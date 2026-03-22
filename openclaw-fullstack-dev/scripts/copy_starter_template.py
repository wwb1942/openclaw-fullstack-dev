#!/usr/bin/env python3
import argparse
import shutil
from pathlib import Path


def assets_dir() -> Path:
    return Path(__file__).resolve().parent.parent / "assets"


def list_templates() -> list[Path]:
    return sorted([p for p in assets_dir().iterdir() if p.is_dir()])


def copy_template(template_name: str, dest: Path, force: bool) -> None:
    source = assets_dir() / template_name
    if not source.exists() or not source.is_dir():
        available = ", ".join(p.name for p in list_templates())
        raise SystemExit(f"Unknown template: {template_name}. Available: {available}")
    if dest.exists():
        if not force:
            raise SystemExit(f"Destination already exists: {dest}. Use --force to overwrite.")
        if dest.is_dir():
            shutil.rmtree(dest)
        else:
            dest.unlink()
    shutil.copytree(source, dest)
    files = [p for p in dest.rglob("*") if p.is_file()]
    print(f"Copied template '{template_name}' to {dest}")
    print(f"Files: {len(files)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy a starter template from the skill assets.")
    parser.add_argument("template", nargs="?", help="Template directory name")
    parser.add_argument("destination", nargs="?", help="Destination path")
    parser.add_argument("--list", action="store_true", help="List available templates")
    parser.add_argument("--force", action="store_true", help="Overwrite destination if it exists")
    args = parser.parse_args()

    if args.list:
        for template in list_templates():
            print(template.name)
        raise SystemExit(0)

    if not args.template or not args.destination:
        parser.error("template and destination are required unless --list is used")

    copy_template(args.template, Path(args.destination).expanduser().resolve(), args.force)
