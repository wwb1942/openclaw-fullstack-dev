import contextlib
import importlib.util
import io
import shutil
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
COPY_SCRIPT_PATH = REPO_ROOT / 'openclaw-fullstack-dev' / 'scripts' / 'copy_starter_template.py'
VERIFY_SCRIPT_PATH = REPO_ROOT / 'openclaw-fullstack-dev' / 'scripts' / 'verify_starter_template.py'

copy_spec = importlib.util.spec_from_file_location('copy_starter_template', COPY_SCRIPT_PATH)
copy_module = importlib.util.module_from_spec(copy_spec)
copy_spec.loader.exec_module(copy_module)

verify_spec = importlib.util.spec_from_file_location('verify_starter_template', VERIFY_SCRIPT_PATH)
verify_module = importlib.util.module_from_spec(verify_spec)
verify_spec.loader.exec_module(verify_module)


class VerifyStarterTemplateTests(unittest.TestCase):
    def test_verify_returns_zero_for_valid_template(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            dest = Path(tmpdir) / 'template'
            copy_module.copy_template('react-express-starter', dest, force=False)
            self.assertEqual(verify_module.verify('react-express-starter', dest), 0)

    def test_verify_reports_missing_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            dest = Path(tmpdir) / 'template'
            copy_module.copy_template('nextjs-nestjs-starter', dest, force=False)
            target = dest / 'server' / 'src' / 'main.ts'
            target.unlink()

            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                code = verify_module.verify('nextjs-nestjs-starter', dest)

            self.assertEqual(code, 1)
            self.assertIn('MISSING server/src/main.ts', buffer.getvalue())


if __name__ == '__main__':
    unittest.main()
