# Employee Directory API

Small FastAPI + SQLite service for looking up employees.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python seed_db.py
```

## Run

```bash
uvicorn app.main:app --reload
```

API docs: http://127.0.0.1:8000/docs

## Endpoints

- `GET /health`
- `GET /employees?department=&skills=&min_salary=` — `skills` is comma-separated, e.g. `Python,SQL`
- `GET /employees/{employee_id}`

## Sample requests

Import `postman/Employee_API.postman_collection.json` into Postman.

## Known issues (reported)

- `GET /employees?skills=Python,SQL` returns the same employee more than once.
- `GET /employees?min_salary=abc` returns `500 Internal Server Error` instead of a client error.
- Negative `min_salary` values are accepted silently.
