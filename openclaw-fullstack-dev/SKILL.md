---
name: openclaw-fullstack-dev
description: Build, refactor, or review full-stack applications in OpenClaw from requirements to a verified MVP. Use when the user asks for a CRUD app, REST API plus frontend, auth flow, file upload, realtime feature, dashboard with backend, monolith vs split frontend/backend decision, production hardening, or end-to-end debugging across frontend, backend, and database. Prefer this skill for multi-step full-stack work that needs architecture choices, staged progress updates, implementation sequencing, verification, and a clean handoff.
---

# openclaw-fullstack-dev

Build full-stack work in a way that survives contact with reality: make explicit decisions, implement the thinnest end-to-end slice first, verify before claiming success, and report with evidence.

## Quick workflow

1. Normalize the request into a concrete target.
2. Choose the project shape and stack defaults.
3. State architecture decisions before major coding.
4. Implement the smallest end-to-end slice.
5. Expand feature-by-feature.
6. Verify build, runtime, and integration.
7. Hand off with commands, files, and known gaps.

Read these references when needed:

- `references/project-shapes.md` — choose monolith vs split repo vs API-only
- `references/verification-checklist.md` — run checks before saying done
- `references/output-contract.md` — keep progress updates and final delivery consistent

## 1. Normalize the target

Extract or infer these fields:

- product goal
- users / audience
- frontend stack
- backend stack
- data store
- auth requirement
- realtime requirement
- file upload / background jobs
- deployment target
- constraints: deadline, existing repo, style, package manager

If the user leaves gaps, infer the safest MVP and say the assumptions explicitly.

Good default assumptions for an MVP:

- frontend: Next.js or React if the repo already uses it
- backend: Node.js service if the repo is JS/TS; otherwise stay within the existing backend stack
- database: SQLite for local MVP, PostgreSQL for multi-user/server work
- auth: omit unless requested; if required, prefer the simplest acceptable flow
- realtime: omit unless clearly needed

## 2. Choose the execution mode

Choose the lightest mode that fits the task:

- **Small fix or narrow feature** — work directly with `read` / `edit` / `exec`
- **Multi-file build or major refactor** — use a coding agent or ACP harness when available
- **Unclear legacy repo** — inspect first, then propose the smallest safe change set

For longer tasks, follow the default OpenClaw progress protocol:

- start confirmation
- stage updates
- blocker alert with options
- final delivery

Do not disappear for a long time without a status update.

## 3. Make architecture decisions up front

Before major implementation, state these decisions in 1-2 lines each:

- project shape
- API style
- data access pattern
- auth strategy
- state management / API client pattern
- realtime method if any
- validation approach
- error handling approach

Prefer these defaults unless the repo or user says otherwise:

- feature-first structure over layer-first
- typed request/response contracts
- schema validation at the boundary
- centralized error handling
- environment variables with `.env.example`
- health endpoint
- explicit loading / empty / error UI states

Use `references/project-shapes.md` if the repo shape is undecided.

## 4. Build the thinnest end-to-end slice first

Do not start with the hardest feature. First make one slice that proves the stack works end to end.

A good first slice usually includes:

1. one backend route or action
2. one storage path or mock data source
3. one frontend screen or component
4. one submit/fetch interaction
5. one visible success state
6. one visible failure state

Examples:

- todo app → create + list one item
- admin dashboard → load one metrics card from backend
- chat app → send and render one message before adding realtime
- file app → upload one file and list it back

## 5. Expand in vertical slices

Add work feature-by-feature, not layer-by-layer.

For each feature slice:

1. define the user action
2. define request/response shape
3. implement backend path
4. implement frontend path
5. add validation and error handling
6. verify manually

Prefer finishing one complete path over half-building five modules.

## 6. Full-stack quality bar

Before calling the work complete, ensure these are present when relevant:

- configuration example file
- install and run commands
- database initialization or migration instructions
- health check or smoke-testable endpoint
- empty/loading/error states in UI
- basic logging or observable failure path
- safe handling for missing env vars
- concise README-style run notes in the final message if no docs file was requested

If auth is requested, also ensure:

- route protection is explicit
- session/token flow is described
- unauthorized and expired-session states are handled

If realtime is requested, also ensure:

- fallback or reconnection behavior is defined
- at least two-client manual verification is attempted when feasible

## 7. Verify before claiming success

Always run some combination of:

- install/build checks
- lint/typecheck when available
- backend start and health check
- frontend start or production build
- one real request through the happy path
- one failure-path check
- integration check between frontend and backend

Use `references/verification-checklist.md` as the default matrix.

If something remains unverified, say so plainly instead of implying it works.

## 8. Handoff

Use the final response to tell the next agent or human exactly what matters:

- what was built
- what assumptions were made
- key files changed
- exact run commands
- exact verification results
- known gaps / next steps

Use `references/output-contract.md` when you want a consistent response shape.

## Guardrails

- Do not claim a full-stack feature works without at least one end-to-end verification step.
- Do not add auth, queues, websockets, or microservices unless the user needs them.
- Do not over-abstract an MVP. Duplicate a little before inventing a framework.
- Do not leave the frontend and backend contracts implicit; write the shapes down in code or prose.
- Do not stall on perfect architecture. Ship the smallest coherent version, then harden.
