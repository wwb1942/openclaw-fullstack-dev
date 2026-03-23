# Starter templates

Use these templates when the user wants a concrete project skeleton instead of pure guidance.

## Available templates

### `nextjs-fastapi-starter`
Use when the user wants a product-oriented UI with a Python backend.

Contents:
- `client/` Next.js page with create + list flow
- `server/` FastAPI app with `GET /health` and basic item endpoints
- top-level `.env.example`
- starter `README.md`

### `react-express-starter`
Use when the user wants a familiar JS/TS split frontend/backend baseline.

Contents:
- `client/` React app entrypoint with create + list flow
- `server/` Express TypeScript entrypoint
- top-level `.env.example`
- starter `README.md`

### `nextjs-nestjs-starter`
Use when the user wants a TypeScript-heavy product stack with a more opinionated backend.

Contents:
- `client/` Next.js page with create + list flow
- `server/` NestJS bootstrap files
- top-level `.env.example`
- starter `README.md`

## Copy a template

```bash
python3 openclaw-fullstack-dev/scripts/copy_starter_template.py --list
python3 openclaw-fullstack-dev/scripts/copy_starter_template.py nextjs-fastapi-starter /tmp/my-app
```

Use `--force` to overwrite an existing destination.

## Verify the copied skeleton

```bash
python3 openclaw-fullstack-dev/scripts/verify_starter_template.py nextjs-fastapi-starter /tmp/my-app
```

For the full checklist, read `references/template-verification.md`.

## Template usage rule

Treat these as starter bones, not finished products. After copying:

1. rename the app
2. wire real env vars
3. replace in-memory demo storage
4. verify health route and one real happy path
5. update README with exact run commands
