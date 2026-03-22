#!/usr/bin/env python3
import argparse
from pathlib import Path

REQUIRED = {
    "nextjs-fastapi-starter": [
        ".env.example",
        "README.md",
        "client/package.json",
        "client/tsconfig.json",
        "client/src/app/layout.tsx",
        "client/src/app/page.tsx",
        "server/requirements.txt",
        "server/app/main.py",
    ],
    "react-express-starter": [
        ".env.example",
        "README.md",
        "client/index.html",
        "client/package.json",
        "client/tsconfig.json",
        "client/src/main.tsx",
        "client/src/App.tsx",
        "server/package.json",
        "server/tsconfig.json",
        "server/src/index.ts",
    ],
    "nextjs-nestjs-starter": [
        ".env.example",
        "README.md",
        "client/package.json",
        "client/tsconfig.json",
        "client/src/app/layout.tsx",
        "client/src/app/page.tsx",
        "server/package.json",
        "server/tsconfig.json",
        "server/nest-cli.json",
        "server/src/main.ts",
    ],
}


def verify(template_name: str, root: Path) -> int:
    missing = [rel for rel in REQUIRED[template_name] if not (root / rel).exists()]
    if missing:
        print(f"Template {template_name}: FAIL")
        for rel in missing:
            print(f"MISSING {rel}")
        return 1
    print(f"Template {template_name}: OK ({len(REQUIRED[template_name])} required files present)")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verify that a copied starter template has all required files.")
    parser.add_argument("template", choices=sorted(REQUIRED.keys()))
    parser.add_argument("path", help="Path to the copied template root")
    args = parser.parse_args()
    raise SystemExit(verify(args.template, Path(args.path).expanduser().resolve()))
