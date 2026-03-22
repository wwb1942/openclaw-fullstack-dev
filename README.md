# openclaw-fullstack-dev

An OpenClaw AgentSkill for building, refactoring, and reviewing full-stack applications with a workflow that favors explicit architecture decisions, thin end-to-end slices, real verification, and clean handoff.

## What this skill is for

Use `openclaw-fullstack-dev` when an agent needs to handle multi-step full-stack work such as:

- building a CRUD app with frontend + backend
- adding auth flows, uploads, or realtime features
- deciding between monolith, split frontend/backend, or API-only shapes
- debugging across UI, server, and database boundaries
- refactoring an existing full-stack codebase into a safer MVP path

The skill is designed to keep agents from jumping straight into code without first clarifying scope, choosing project shape, and defining a verification plan.

## Core workflow

1. Normalize the request into a concrete implementation target
2. Choose project shape and stack defaults
3. State architecture decisions before major coding
4. Build the thinnest end-to-end slice first
5. Expand feature-by-feature in vertical slices
6. Verify build, runtime, and integration
7. Hand off with commands, changed files, assumptions, and gaps

## Practical resources included

### 1. Kickoff plan script

Generate a structured first-pass plan before coding:

```bash
python3 openclaw-fullstack-dev/scripts/generate_fullstack_plan.py \
  "Build an internal feedback tracker with Next.js, FastAPI, and PostgreSQL" \
  --frontend nextjs \
  --backend fastapi \
  --db postgres
```

### 2. Stack guides

- `references/stack-nextjs-fastapi.md`
- `references/stack-react-express.md`
- `references/stack-nextjs-nestjs.md`

These provide a sane default project shape, first vertical slice, implementation notes, and verification commands.

### 3. Starter templates

This repo now includes copyable starter templates under `openclaw-fullstack-dev/assets/`:

- `nextjs-fastapi-starter`
- `react-express-starter`
- `nextjs-nestjs-starter`

Copy one into a working directory with:

```bash
python3 openclaw-fullstack-dev/scripts/copy_starter_template.py --list
python3 openclaw-fullstack-dev/scripts/copy_starter_template.py nextjs-fastapi-starter /tmp/my-app
```

### 4. Demo task

See `references/demo-task.md` for a concrete example request, normalized target, kickoff command, and completion expectations.

## Repository layout

```text
openclaw-fullstack-dev/
├── openclaw-fullstack-dev/
│   ├── SKILL.md
│   ├── assets/
│   │   ├── nextjs-fastapi-starter/
│   │   ├── nextjs-nestjs-starter/
│   │   └── react-express-starter/
│   ├── references/
│   │   ├── demo-task.md
│   │   ├── output-contract.md
│   │   ├── project-shapes.md
│   │   ├── stack-nextjs-fastapi.md
│   │   ├── stack-nextjs-nestjs.md
│   │   ├── stack-react-express.md
│   │   ├── starter-templates.md
│   │   └── verification-checklist.md
│   └── scripts/
│       ├── copy_starter_template.py
│       └── generate_fullstack_plan.py
└── dist/
    └── openclaw-fullstack-dev.skill
```

## Packaging

Rebuild the `.skill` package with:

```bash
python3 /usr/lib/node_modules/openclaw/skills/skill-creator/scripts/package_skill.py ./openclaw-fullstack-dev ./dist
```

## Design goals

This skill intentionally pushes agents toward:

- explicit assumptions
- architecture before implementation
- smallest viable end-to-end slice first
- verification before confidence
- concise but operational handoff
- copying a starter only when it genuinely helps

## Status

Current version: practical v1 with workflow guidance, starter resources, and boilerplate templates.
