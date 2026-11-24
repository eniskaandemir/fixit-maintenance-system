# FixIt — Apartment Maintenance Request System

Semester project for **Software Development Methodologies**.

FixIt is a small web application for apartment maintenance requests. Residents can report a problem and track its progress; a property manager can review and process submitted requests.

## Product goal
Provide residents with a simple and transparent way to report maintenance problems and track their resolution while giving property management a centralized workflow for organizing requests.

## Core users
- **Resident:** creates and tracks maintenance requests.
- **Property Manager:** reviews requests and manages their progress.

## Core workflow
Resident submits request → Manager reviews request → Status changes → Resident sees progress.

Planned statuses: `New → Assigned → In Progress → Resolved`.

## Initial scope
- Authentication and user roles
- Create maintenance request
- Resident request list
- Manager request list
- Request details
- Status and priority
- Filtering
- Automated tests
- CI with GitHub Actions

## Out of scope for the semester MVP
Payments, rent management, native mobile apps, AI diagnosis, IoT integrations, real-time chat, automatic technician scheduling, and enterprise multi-property management.

## Development method
**Scrum with selected XP practices**: short iterations, visible backlog, automated testing, continuous integration, small changes, and code review where another reviewer is available.

## Board workflow
`Backlog → Ready → In Progress → Review → Done`

## Definition of Done
An item is Done when its acceptance criteria are met, relevant tests pass, existing tests remain green, documentation is updated when needed, the work is traceable to an issue/commit/PR, CI passes, and the change is merged into `main`.

## Sprint 1 goal
Deliver the first usable end-to-end maintenance reporting flow: a resident can submit a maintenance request and a property manager can see the submitted request.

## Technology stack
- Python
- Flask
- SQLite
- SQLAlchemy (planned)
- HTML/CSS
- pytest
- GitHub Actions

## Run locally
```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Install:
```bash
pip install -r requirements.txt
```

Run:
```bash
python run.py
```

Tests:
```bash
pytest
```

## Project records
See:
- [Project documentation](docs/PROJECT_DOCUMENTATION.md)
- [Checkpoint 01 evidence](docs/CHECKPOINT_01.md)

## Working mode note
This repository is currently being completed **individually**. The course brief normally expects a team of 3–5 students. Therefore, peer-review/team-rotation evidence cannot be represented as completed unless another student actually participates. Automated CI and documented self-review are used instead where possible.
