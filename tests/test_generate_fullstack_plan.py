import argparse
import importlib.util
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / 'openclaw-fullstack-dev' / 'scripts' / 'generate_fullstack_plan.py'

spec = importlib.util.spec_from_file_location('generate_fullstack_plan', SCRIPT_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class GenerateFullstackPlanTests(unittest.TestCase):
    def test_default_shape_prefers_api_only_when_no_frontend(self):
        self.assertEqual(module.default_shape('none', 'fastapi'), 'api-only')

    def test_default_shape_detects_monolith_for_nextjs_api(self):
        self.assertEqual(module.default_shape('nextjs', 'nextjs-api'), 'monolith')

    def test_default_db_uses_sqlite_for_monolith(self):
        self.assertEqual(module.default_db('monolith'), 'sqlite')
        self.assertEqual(module.default_db('split'), 'postgres')

    def test_default_package_manager_prefers_pnpm_for_modern_frontends(self):
        self.assertEqual(module.default_package_manager('react-vite'), 'pnpm')
        self.assertEqual(module.default_package_manager('vue'), 'pnpm')
        self.assertEqual(module.default_package_manager('htmx'), 'npm')

    def test_render_includes_normalized_decisions_and_verification_commands(self):
        args = argparse.Namespace(
            goal='Build an internal admin tool',
            frontend='nextjs',
            backend='fastapi',
            shape=None,
            db=None,
            auth='session',
            realtime='sse',
            package_manager=None,
        )

        output = module.render(args)

        self.assertIn('project shape: **split**', output)
        self.assertIn('database: **postgres**', output)
        self.assertIn('auth: **session**', output)
        self.assertIn('realtime: **sse**', output)
        self.assertIn('`cd server && python -m uvicorn app.main:app --reload`', output)
        self.assertIn('`cd client && pnpm install && pnpm build`', output)


if __name__ == '__main__':
    unittest.main()
