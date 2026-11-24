# Checkpoint 01 — Evidence

Project: **FixIt — Apartment Maintenance Request System**

## Product goal
Provide residents with a simple and transparent way to report maintenance problems and track their resolution while giving property management a centralized workflow for organizing requests.

## Method
Scrum with selected XP practices (automated testing, CI, small changes, review discipline).

## Evidence links

- Repository: https://github.com/eniskaandemir/fixit-maintenance-system
- Project record: [PROJECT_DOCUMENTATION.md](PROJECT_DOCUMENTATION.md)
- Issues/backlog: https://github.com/eniskaandemir/fixit-maintenance-system/issues
- Project board: **To be created manually in GitHub Projects**
- Sprint 0 implementation issue: https://github.com/eniskaandemir/fixit-maintenance-system/issues/8
- Feature branch: https://github.com/eniskaandemir/fixit-maintenance-system/tree/feature/8-app-skeleton
- Pull request: https://github.com/eniskaandemir/fixit-maintenance-system/pull/9
- Automated tests: https://github.com/eniskaandemir/fixit-maintenance-system/blob/main/tests/test_app.py
- CI workflow: https://github.com/eniskaandemir/fixit-maintenance-system/blob/main/.github/workflows/ci.yml
- Actions runs: https://github.com/eniskaandemir/fixit-maintenance-system/actions

## Traceability
Issue #8 → branch `feature/8-app-skeleton` → implementation commits → PR #9 → documented self-review → squash merge to `main`.

## Board workflow
`Backlog → Ready → In Progress → Review → Done`

## Sprint 1 goal
Deliver the first usable end-to-end maintenance reporting flow: resident submits a request and property manager can see it.

## Individual-work disclosure
The repository is currently being developed individually. The course brief normally expects a 3–5 person team and a reviewed PR. No teammate or peer review is invented. PR #9 includes a documented self-review, while automated CI is used as an additional quality check. This is an honest adaptation of the required process, not a claim that peer review occurred.
