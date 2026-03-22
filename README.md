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

## Repository layout

```text
openclaw-fullstack-dev/
├── openclaw-fullstack-dev/
│   ├── SKILL.md
│   └── references/
│       ├── output-contract.md
│       ├── project-shapes.md
│       └── verification-checklist.md
└── dist/
    └── openclaw-fullstack-dev.skill
```

## Included files

- `openclaw-fullstack-dev/SKILL.md` — main skill instructions and workflow
- `openclaw-fullstack-dev/references/project-shapes.md` — when to use monolith vs split vs API-only
- `openclaw-fullstack-dev/references/verification-checklist.md` — minimum verification bar before claiming success
- `openclaw-fullstack-dev/references/output-contract.md` — start / progress / blocker / final delivery structure
- `dist/openclaw-fullstack-dev.skill` — packaged distributable artifact

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

## Status

Current version: early skeleton, but already usable as a workflow-oriented OpenClaw skill.
