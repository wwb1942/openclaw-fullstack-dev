# nextjs-fastapi-starter

Split full-stack starter with a Next.js client and a FastAPI server.
This starter now includes the smallest useful browser loop: create an item and see it rendered back immediately.

## Structure

- `client/` — Next.js UI
- `server/` — FastAPI API
- `.env.example` — default environment variables

## First slice included

- backend health route
- basic item create/list API
- frontend page with create + list flow

## Run

```bash
# server
cd server
# use venv, uv, or another environment manager if you prefer isolation
pip install -r requirements.txt
uvicorn app.main:app --reload

# client
cd client
npm install
npm run dev
```

## Next steps

1. replace in-memory data with a real database
2. add validation and error UI
3. add tests and deployment setup
