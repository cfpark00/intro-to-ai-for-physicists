# CLAUDE.md

This is the **public textbook source**. The book is built with Quarto from `src/` and published to <https://scienceofdl.com> via GitHub Actions on push to `main`.

Keep this repo clean of dev-process artifacts. Workflow conventions, project context, course-design gists, session logs, per-lecture authoring plans, and Slurm orchestration all live in the private sibling repo at `../scidl-dev/`. Read `../scidl-dev/docs/repo_usage.md` and `../scidl-dev/docs/context.md` for anything that crosses both repos.

Scope of changes that belong here: prose and code under `src/`, deploy CI under `.github/`, Python env (`pyproject.toml`/`uv.lock`), and the public `README.md`.
