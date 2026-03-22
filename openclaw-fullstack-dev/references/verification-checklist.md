# Verification checklist

Run the smallest useful set of checks that proves the feature works.

## Minimum bar for most tasks

- install dependencies successfully
- build or typecheck passes if the project provides it
- backend starts without crashing
- frontend starts or production build succeeds
- one happy-path user flow works end to end
- one failure path is checked

## Backend checks

Examples:

```bash
npm run build
npm run test
curl http://localhost:3000/health
curl http://localhost:3000/api/items
```

Verify:

- process starts
- health route responds
- validation errors are readable
- missing env vars fail loudly and clearly

## Frontend checks

Examples:

```bash
npm run build
npm run lint
```

Verify:

- page renders without fatal errors
- loading state appears when expected
- empty state is sensible
- error state is visible and not swallowed

## Integration checks

Verify:

- frontend uses the correct API base URL
- CORS/auth/session behavior matches the architecture
- create/update/delete flows reflect in the UI
- backend errors surface as meaningful UI messages

## Realtime checks

When applicable:

- open two clients
- trigger one update
- verify the second client reflects the change
- verify reconnect or fallback behavior if practical

## If verification is incomplete

Say exactly what was not verified and why.
Bad: "should work"
Good: "backend build passed and the route responded via curl; browser-side integration was not run in this environment"
