from fastapi import FastAPI, HTTPException
from database import get_connection, initialize_database

app = FastAPI()

initialize_database()


VALID_SEVERITIES = {"P0", "P1", "P2", "P3"}
VALID_STATUSES = {"Open", "Closed"}


@app.get("/")
def health_check():
    return {"status": "QA Bug API is running"}


@app.get("/bugs")
def get_bugs():
    connection = get_connection()

    rows = connection.execute(
        "SELECT id, title, severity, status FROM bugs"
    ).fetchall()

    connection.close()

    return {"bugs": [dict(row) for row in rows]}

@app.get("/bugs/summary")
def get_bug_summary():
    connection = get_connection()

    rows = connection.execute(
        """
        SELECT severity, COUNT(*) AS count
        FROM bugs
        WHERE status = 'Open'
        GROUP BY severity
        ORDER BY severity
        """
    ).fetchall()

    connection.close()

    return {
        row["severity"]: row["count"]
        for row in rows
    }


@app.post("/bugs", status_code=201)
def create_bug(bug: dict):
    title = bug.get("title")
    severity = bug.get("severity")
    status = bug.get("status")

    if not title:
        raise HTTPException(status_code=400, detail="Title is required")

    if severity not in VALID_SEVERITIES:
        raise HTTPException(status_code=400, detail="Invalid severity")

    if status not in VALID_STATUSES:
        raise HTTPException(status_code=400, detail="Invalid status")

    connection = get_connection()

    cursor = connection.execute(
        """
        INSERT INTO bugs (title, severity, status)
        VALUES (?, ?, ?)
        """,
        (title, severity, status),
    )

    connection.commit()

    bug_id = cursor.lastrowid

    connection.close()

    return {
        "id": bug_id,
        "title": title,
        "severity": severity,
        "status": status,
    }