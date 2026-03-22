# Stack guide: Next.js + FastAPI

Use this stack when the user wants a fast-moving product UI plus a Python backend for APIs, data processing, or AI-heavy endpoints.

## Recommended shape

Prefer **split frontend + backend**:

- `client/` → Next.js app
- `server/` → FastAPI service
- optional `shared/` → API contracts, generated types, or examples

## Good defaults

- frontend: Next.js App Router + TypeScript
- backend: FastAPI + Pydantic
- database: PostgreSQL for shared/server work, SQLite for a local MVP
- auth: omit unless required; otherwise start with session or bearer token, not both

## First vertical slice

Build this before advanced features:

1. `GET /health`
2. one resource with `POST /api/items` and `GET /api/items`
3. one Next.js page with a form and a list
4. explicit loading / empty / error states

## Key implementation notes

- Keep request/response models in Pydantic at the API boundary
- Centralize API calls in one client module on the Next.js side
- Use env vars for `NEXT_PUBLIC_API_BASE_URL`
- Do not hide backend failures; surface them in the page UI

## Verification

```bash
# server
cd server && python -m uvicorn app.main:app --reload
curl http://localhost:8000/health

# client
cd client && pnpm install && pnpm build
```

Then verify the page can create one item and render it back from the API.
