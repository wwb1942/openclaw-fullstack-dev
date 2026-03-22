# Template verification

Use this when you copied a starter template and want a deterministic sanity check before further editing.

## Verify a copied template

```bash
python3 openclaw-fullstack-dev/scripts/verify_starter_template.py nextjs-fastapi-starter /tmp/my-app
python3 openclaw-fullstack-dev/scripts/verify_starter_template.py react-express-starter /tmp/my-react-app
python3 openclaw-fullstack-dev/scripts/verify_starter_template.py nextjs-nestjs-starter /tmp/my-nest-app
```

## What this check guarantees

- required starter files exist
- the copied project has the expected skeleton shape

## What it does not guarantee

- dependencies install successfully
- TypeScript or framework build passes
- runtime behavior is correct

Use this as a fast preflight check, not as full validation.
