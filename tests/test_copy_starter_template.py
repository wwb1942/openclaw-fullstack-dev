import importlib.util
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / 'openclaw-fullstack-dev' / 'scripts' / 'copy_starter_template.py'

spec = importlib.util.spec_from_file_location('copy_starter_template', SCRIPT_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CopyStarterTemplateTests(unittest.TestCase):
    def test_list_templates_contains_all_expected_starters(self):
        names = [path.name for path in module.list_templates()]
        self.assertEqual(
            names,
            ['nextjs-fastapi-starter', 'nextjs-nestjs-starter', 'react-express-starter'],
        )

    def test_copy_template_copies_expected_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            dest = Path(tmpdir) / 'copied-template'
            module.copy_template('nextjs-fastapi-starter', dest, force=False)
            self.assertTrue((dest / 'client' / 'src' / 'app' / 'page.tsx').exists())
            self.assertTrue((dest / 'server' / 'app' / 'main.py').exists())

    def test_copy_template_rejects_unknown_template(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            dest = Path(tmpdir) / 'missing-template'
            with self.assertRaises(SystemExit) as ctx:
                module.copy_template('unknown-template', dest, force=False)
            self.assertIn('Unknown template', str(ctx.exception))

    def test_copy_template_rejects_existing_destination_without_force(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            dest = Path(tmpdir) / 'existing'
            dest.mkdir()
            with self.assertRaises(SystemExit) as ctx:
                module.copy_template('react-express-starter', dest, force=False)
            self.assertIn('Destination already exists', str(ctx.exception))


if __name__ == '__main__':
    unittest.main()
