# Stack guide: Next.js + NestJS

Use this stack when the user wants a TypeScript-heavy product stack with a more opinionated backend structure, modules, and enterprise-style extension points.

## Recommended shape

Prefer **split frontend + backend** unless the repo already uses Next-only APIs.

- `client/` → Next.js
- `server/` → NestJS

## Good defaults

- frontend: Next.js App Router + TypeScript
- backend: NestJS modules per feature
- validation: DTOs + class-validator or zod at boundaries
- database: PostgreSQL for most real apps
- auth: session or JWT, chosen explicitly before coding

## First vertical slice

1. `GET /health`
2. one NestJS feature module with create + list
3. one Next.js page that consumes the feature endpoints
4. visible loading, empty, success, and error states

## Key implementation notes

- Avoid overengineering the first slice with too many shared abstractions
- Keep DTOs and response shapes stable before adding more modules
- Add one clear env contract for API base URL and secrets
- If auth is requested, handle unauthorized and expired-session states explicitly

## Verification

```bash
# server
cd server && npm install && npm run build
curl http://localhost:3001/health

# client
cd client && pnpm install && pnpm build
```

Then verify one real page-to-API interaction before adding more modules.
