# Stack guide: React + Express

Use this stack when the user wants a familiar JavaScript/TypeScript split with a lightweight backend and a decoupled SPA frontend.

## Recommended shape

Prefer **split frontend + backend**:

- `client/` → React app (often Vite)
- `server/` → Express service
- optional `shared/` → shared schemas or DTOs

## Good defaults

- frontend: React + Vite + TypeScript
- backend: Express + TypeScript
- validation: zod or another boundary schema tool
- database: SQLite for quick local CRUD, PostgreSQL when multi-user or deployment is expected

## First vertical slice

1. `GET /health`
2. one feature route pair: create + list
3. one React screen with submit + render
4. one handled error path from server to UI

## Key implementation notes

- Keep route handlers thin; push domain logic into feature modules
- Prefer feature-first layout over controller/service/repository sprawl
- Use one API client wrapper on the React side
- Add CORS intentionally; do not leave it implicit

## Verification

```bash
# server
cd server && npm install && npm run build
curl http://localhost:3001/health

# client
cd client && npm install && npm run build
```

Then manually verify create/list flow and one validation error path.
