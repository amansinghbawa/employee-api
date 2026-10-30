"""Create and populate employees.db with synthetic data. Safe to re-run."""
from app.database import DB_PATH, get_connection

DEPARTMENTS = ["Engineering", "Data", "Marketing", "Finance"]

# (name, email, department, title, salary)
EMPLOYEES = [
    ("Alice Carter", "alice.carter@example.com", "Engineering", "Senior Backend Engineer", 125000),
    ("Ben Ortiz", "ben.ortiz@example.com", "Engineering", "Backend Engineer", 98000),
    ("Chloe Nguyen", "chloe.nguyen@example.com", "Data", "Data Analyst", 82000),
    ("David Kim", "david.kim@example.com", "Data", "Data Engineer", 110000),
    ("Emma Rossi", "emma.rossi@example.com", "Marketing", "Marketing Manager", 90000),
    ("Farah Haddad", "farah.haddad@example.com", "Finance", "Financial Analyst", 76000),
    ("George Patel", "george.patel@example.com", "Engineering", "Frontend Engineer", 95000),
    ("Hana Sato", "hana.sato@example.com", "Finance", "Finance Lead", 118000),
]

SKILLS = {
    "alice.carter@example.com": ["Python", "SQL", "FastAPI"],
    "ben.ortiz@example.com": ["Python", "Docker"],
    "chloe.nguyen@example.com": ["SQL", "Excel"],
    "david.kim@example.com": ["Python", "SQL", "Spark"],
    "emma.rossi@example.com": ["SEO", "Excel"],
    "farah.haddad@example.com": ["Excel", "SQL"],
    "george.patel@example.com": ["JavaScript", "React"],
    "hana.sato@example.com": ["Excel", "Python"],
}


def seed():
    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = get_connection()
    cur = conn.cursor()
    cur.executescript(
        """
        CREATE TABLE departments (
            id   INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
        CREATE TABLE employees (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            name          TEXT NOT NULL,
            email         TEXT NOT NULL UNIQUE,
            department_id INTEGER NOT NULL REFERENCES departments(id),
            title         TEXT NOT NULL,
            salary        INTEGER NOT NULL
        );
        CREATE TABLE employee_skills (
            employee_id INTEGER NOT NULL REFERENCES employees(id),
            skill       TEXT NOT NULL,
            PRIMARY KEY (employee_id, skill)
        );
        """
    )

    dept_ids = {}
    for name in DEPARTMENTS:
        cur.execute("INSERT INTO departments (name) VALUES (?)", (name,))
        dept_ids[name] = cur.lastrowid

    for name, email, dept, title, salary in EMPLOYEES:
        cur.execute(
            "INSERT INTO employees (name, email, department_id, title, salary) VALUES (?, ?, ?, ?, ?)",
            (name, email, dept_ids[dept], title, salary),
        )
        emp_id = cur.lastrowid
        for skill in SKILLS[email]:
            cur.execute(
                "INSERT INTO employee_skills (employee_id, skill) VALUES (?, ?)",
                (emp_id, skill),
            )

    conn.commit()
    conn.close()
    print(f"Seeded {len(EMPLOYEES)} employees into {DB_PATH}")


if __name__ == "__main__":
    seed()
