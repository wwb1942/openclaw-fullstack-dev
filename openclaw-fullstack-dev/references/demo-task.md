# Demo task

Use this example to understand how the skill should behave.

## Example request

> Build a small internal feedback tracker with a web UI, FastAPI backend, and PostgreSQL. Users should be able to create feedback items and mark them resolved later.

## Normalized target

- product goal: internal feedback tracker
- frontend: Next.js
- backend: FastAPI
- database: PostgreSQL
- auth: none for MVP
- realtime: none
- shape: split frontend + backend

## Expected first slice

1. health endpoint
2. create feedback item
3. list feedback items
4. page with submit form + list
5. loading / empty / error states

## Example kickoff plan command

```bash
python3 openclaw-fullstack-dev/scripts/generate_fullstack_plan.py \
  "Build an internal feedback tracker with Next.js, FastAPI, and PostgreSQL" \
  --frontend nextjs \
  --backend fastapi \
  --db postgres
```

## What a good completion should mention

- assumptions kept for the MVP
- files changed in client and server
- how to run both services
- exact verification performed
- remaining work such as auth, edit/delete, deployment, and tests
