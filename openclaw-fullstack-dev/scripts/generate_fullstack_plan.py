#!/usr/bin/env python3
import argparse


def default_shape(frontend: str, backend: str) -> str:
    if frontend in {"none", "api-only"}:
        return "api-only"
    if frontend.startswith("nextjs") and backend in {"nextjs-api", "same-as-frontend"}:
        return "monolith"
    return "split"


def default_db(shape: str) -> str:
    return "sqlite" if shape == "monolith" else "postgres"


def default_package_manager(frontend: str) -> str:
    if frontend.startswith(("nextjs", "react", "vue")):
        return "pnpm"
    return "npm"


def backend_verification_commands(backend: str, shape: str):
    if shape == "monolith":
        return [
            "pnpm install",
            "pnpm build",
            "pnpm lint",
            "curl http://localhost:3000/api/health",
        ]

    mapping = {
        "fastapi": [
            "cd server && python -m pytest || true",
            "cd server && python -m uvicorn app.main:app --reload",
            "curl http://localhost:8000/health",
        ],
        "express": [
            "cd server && npm install && npm run build",
            "curl http://localhost:3001/health",
        ],
        "nestjs": [
            "cd server && npm install && npm run build",
            "curl http://localhost:3001/health",
        ],
    }
    return mapping.get(backend, ["cd server && <run backend build/start>", "curl <backend health endpoint>"])


def frontend_verification_commands(shape: str, frontend: str, package_manager: str):
    if shape == "api-only" or frontend in {"none", "api-only"}:
        return []
    if shape == "monolith":
        return []
    install = f"cd client && {package_manager} install && {package_manager} build"
    return [install]


def bullet(items):
    return "\n".join(f"- {item}" for item in items)


def render(args):
    shape = args.shape or default_shape(args.frontend, args.backend)
    db = args.db or default_db(shape)
    package_manager = args.package_manager or default_package_manager(args.frontend)
    auth = args.auth or "none"
    realtime = args.realtime or "none"

    first_slice = [
        "one health/status endpoint",
        "one persisted resource with create + list",
        "one frontend page to submit and render data",
        "visible loading, empty, success, and error states",
    ]

    verification = []
    verification.append("# backend")
    verification.extend(backend_verification_commands(args.backend, shape))
    frontend_commands = frontend_verification_commands(shape, args.frontend, package_manager)
    if frontend_commands:
        verification.append("# frontend")
        verification.extend(frontend_commands)

    sections = [
        "# Full-stack kickoff plan",
        "",
        "## Goal",
        args.goal,
        "",
        "## Normalized decisions",
        bullet([
            f"project shape: **{shape}**",
            f"frontend: **{args.frontend}**",
            f"backend: **{args.backend}**",
            f"database: **{db}**",
            f"auth: **{auth}**",
            f"realtime: **{realtime}**",
            f"package manager: **{package_manager}**",
        ]),
        "",
        "## Suggested first vertical slice",
        bullet(first_slice),
        "",
        "## Delivery order",
        "1. scaffold folders and environment files",
        "2. implement backend health route and one resource route",
        "3. connect frontend page to the backend",
        "4. add boundary validation and user-facing error states",
        "5. verify happy path and one failure path",
        "",
        "## Key files to expect",
        bullet([
            "`.env.example`",
            "`README.md`",
            "backend entrypoint and health route",
            "frontend page for the first slice",
            "schema/model definition for the first resource",
        ]),
        "",
        "## Verification commands",
        bullet([f"`{cmd}`" for cmd in verification]),
        "",
    ]
    return "\n".join(sections)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a deterministic kickoff plan for a full-stack project.")
    parser.add_argument("goal", help="Project goal in natural language")
    parser.add_argument("--frontend", default="nextjs", help="Frontend stack, e.g. nextjs, react-vite, vue")
    parser.add_argument("--backend", default="fastapi", help="Backend stack, e.g. fastapi, express, nestjs, nextjs-api")
    parser.add_argument("--shape", choices=["monolith", "split", "api-only"], help="Project shape")
    parser.add_argument("--db", help="Database choice")
    parser.add_argument("--auth", help="Auth mode, e.g. none, jwt, session, clerk")
    parser.add_argument("--realtime", help="Realtime mode, e.g. none, sse, websocket")
    parser.add_argument("--package-manager", help="Package manager, e.g. npm, pnpm, yarn")
    args = parser.parse_args()
    print(render(args), end="")
