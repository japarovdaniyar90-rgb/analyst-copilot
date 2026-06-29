# AGENTS.md

This repository contains the project "Analyst Copilot".

Before implementing any task, ALWAYS read:

1. docs/PRD.md
2. docs/ARCHITECTURE.md
3. docs/ENGINEERING_GUIDE.md
4. docs/BACKLOG.md
5. docs/tasks/*.md (current task)

## Rules

- Follow Clean Architecture.
- Telegram is Presentation Layer only.
- Business logic belongs to Services.
- Storage contains persistence only.
- Use Pydantic models.
- Use Python 3.14.
- Use typing everywhere.
- Do not introduce unnecessary dependencies.
- Keep files under ~200 lines when practical.
- Do not rewrite unrelated code.
- Change only files required by the task.
- Explain architectural decisions after implementation.

## Workflow

For every task:

Read documentation.

Implement task.

Run tests if available.

Explain changes.

Wait for review.