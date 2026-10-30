from typing import List, Optional

from fastapi import FastAPI, HTTPException

from app.database import get_connection
from app.models import Employee

app = FastAPI(title="Employee Directory API", version="1.0.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/employees", response_model=List[Employee])
def list_employees(
    department: Optional[str] = None,
    skills: Optional[str] = None,
    min_salary: Optional[str] = None,
):
    """
    Retrieve employees, optionally filtered by:
      - department: exact department name (e.g. "Engineering")
      - skills: comma-separated list of skills (e.g. "Python,SQL")
      - min_salary: minimum annual salary
    """
    query = """
        SELECT e.id, e.name, e.email, d.name AS department, e.title, e.salary
        FROM employees e
        JOIN departments d ON d.id = e.department_id
    """
    conditions = []
    params = []

    if skills:
        skill_list = [s.strip() for s in skills.split(",")]
        query += " JOIN employee_skills es ON es.employee_id = e.id"
        placeholders = ",".join("?" for _ in skill_list)
        conditions.append(f"es.skill IN ({placeholders})")
        params.extend(skill_list)

    if department:
        conditions.append("d.name = ?")
        params.append(department)

    if min_salary:
        conditions.append("e.salary >= ?")
        params.append(int(min_salary))

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    query += " ORDER BY e.id"

    conn = get_connection()
    try:
        rows = conn.execute(query, params).fetchall()
    finally:
        conn.close()

    return [dict(row) for row in rows]


@app.get("/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: int):
    conn = get_connection()
    try:
        row = conn.execute(
            """
            SELECT e.id, e.name, e.email, d.name AS department, e.title, e.salary
            FROM employees e
            JOIN departments d ON d.id = e.department_id
            WHERE e.id = ?
            """,
            (employee_id,),
        ).fetchone()
    finally:
        conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return dict(row)
