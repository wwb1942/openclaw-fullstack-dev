# Project shapes

Use this file when deciding how to structure a full-stack project.

## 1. API-only backend

Choose this when:

- the user only asked for backend work
- the frontend already exists elsewhere
- another team owns the UI
- the immediate goal is integrations or automation

Default shape:

- `src/features/<feature>/`
- `src/lib/`
- `src/config/`
- `src/server/` or `src/http/`

## 2. Full-stack monolith

Choose this when:

- the app is small to medium
- one team owns frontend and backend
- deployment simplicity matters
- speed is more important than service separation

Good default for:

- internal tools
- dashboards
- CRUD apps
- admin panels
- authenticated MVPs

Default shape:

- `app/` or `src/app/` for UI routes
- `src/features/` for domain logic
- `src/server/` for backend-only modules
- `src/lib/` for shared helpers
- `db/` or `prisma/` for schema/migrations

## 3. Split frontend + backend

Choose this when:

- the frontend and backend deploy separately
- the backend must serve multiple clients
- the repo already has this split
- ownership boundaries are important

Default shape:

- `client/`
- `server/`
- optional `shared/` for types or contracts

## Decision heuristics

Prefer a monolith when the user asks for a new MVP and no strong reason to split exists.
Prefer split services when the repo already uses that shape or multiple clients depend on the backend.
Prefer API-only when UI work is explicitly out of scope.

## Anti-patterns

Avoid these unless the task truly needs them:

- microservices for an MVP
- generic repository/service/controller abstractions everywhere
- adding GraphQL, queues, or websockets without a concrete requirement
- creating a shared package too early when only one consumer exists
