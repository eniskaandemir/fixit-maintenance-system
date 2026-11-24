# Sprint 0 Record — FixIt

## Project overview

**FixIt — Apartment Maintenance Request System** is a small web application for reporting and tracking apartment maintenance problems.

Residents can submit maintenance requests and follow their progress. Property managers can review incoming requests and manage them through a simple workflow.

The first semester increment focuses on the core reporting flow rather than optional features such as payments, AI diagnosis, IoT integration, native mobile applications, real-time chat, or automatic technician scheduling.

## Project links

- Repository: https://github.com/eniskaandemir/fixit-maintenance-system
- Issue backlog: https://github.com/eniskaandemir/fixit-maintenance-system/issues
- Project board: https://github.com/users/eniskaandemir/projects/1
- Project documentation: https://github.com/eniskaandemir/fixit-maintenance-system/blob/main/docs/PROJECT_DOCUMENTATION.md
- Setup instructions: https://github.com/eniskaandemir/fixit-maintenance-system/blob/main/README.md

## Product and planning

The product goal, target users, scope, assumptions, risks, user journeys, glossary, and initial domain model are maintained in the project documentation.

The backlog is ordered by user value, dependency, risk, and ability to demonstrate a complete workflow. The first planned vertical slice is:

**Resident submits a maintenance request → Property manager can see the submitted request**

Acceptance criteria are documented for the highest-priority stories. The project also records measurable quality scenarios for response time, authorization, and input validation.

## Development approach

The project uses **Scrum with selected XP practices**.

Scrum provides the iteration structure for Sprint 0 and the three implementation sprints. XP-inspired practices such as automated testing, continuous integration, small changes, and review discipline are used to support technical quality.

Board workflow:

`Backlog → Ready → In Progress → Review → Done`

The Definition of Done requires acceptance criteria to be satisfied, relevant tests to pass, CI to be green, documentation to be updated where needed, and the change to be traceable to repository work.

## Sprint 0 technical setup

Sprint 0 established the initial project structure and development workflow.

Main evidence:

- Sprint 0 setup issue: https://github.com/eniskaandemir/fixit-maintenance-system/issues/8
- Sprint 0 pull request: https://github.com/eniskaandemir/fixit-maintenance-system/pull/9
- Automated tests: https://github.com/eniskaandemir/fixit-maintenance-system/blob/main/tests/test_app.py
- CI workflow: https://github.com/eniskaandemir/fixit-maintenance-system/blob/main/.github/workflows/ci.yml
- Successful CI run: https://github.com/eniskaandemir/fixit-maintenance-system/actions/runs/45414379868

The first CI attempt exposed a Python import-path problem. The problem was kept visible and handled through a separate issue and pull request:

- CI fix issue: https://github.com/eniskaandemir/fixit-maintenance-system/issues/10
- CI fix pull request: https://github.com/eniskaandemir/fixit-maintenance-system/pull/11

The corrected workflow passed successfully after the fix.

## Sprint 0 review

Sprint 0 completed the intended setup work:

- repository and README created,
- backlog and project workflow established,
- project documentation started,
- minimal Flask application skeleton created,
- automated smoke tests added,
- GitHub Actions CI configured,
- issue-to-branch-to-PR traceability demonstrated.

The main technical problem discovered during Sprint 0 was the failed test import in CI. Finding this during setup was useful because it was corrected before Sprint 1 implementation work began.

## Retrospective action

For Sprint 1, an issue should only move to **Done** after its acceptance criteria have been checked, relevant automated tests have been added where practical, and CI is confirmed green.

## Sprint 1 goal

Deliver the first usable end-to-end maintenance reporting flow:

**a resident can submit a maintenance request and a property manager can see the submitted request.**

## Working mode note

The project is currently being completed individually. Repository history therefore records self-review and automated CI checks rather than claiming a peer review that did not occur.
