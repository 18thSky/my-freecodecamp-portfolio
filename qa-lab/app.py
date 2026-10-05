from fastapi import FastAPI, HTTPException

from database import get_connection, initialize_database


app = FastAPI()

initialize_database()


VALID_SEVERITIES = {
    "Low",
    "Medium",
    "High",
    "Urgent",
}

VALID_STATUSES = {
    "Bugged",
    "Existing Bug",
    "Non-Recreatable",
    "Bug verified/QA Pass",
    "QC Change",
    "Bug fixed",
    "New Req",
    "Not a bug",
}

OPEN_STATUSES = {
    "Bugged",
    "Existing Bug",
    "Non-Recreatable",
    "QC Change",
    "New Req",
}


@app.get("/")
def health_check():
    return {
        "status": "QA Bug API is running"
    }


@app.get("/bugs")
def get_bugs():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT
                id,
                title,
                severity,
                status,
                priority_by_qa,
                priority_by_product,
                dev_assigned
            FROM bugs
            ORDER BY id
            """
        )

        rows = cursor.fetchall()

        return {
            "bugs": rows
        }

    finally:
        cursor.close()
        connection.close()


@app.get("/bugs/summary")
def get_bug_summary():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT
                severity,
                COUNT(*) AS count
            FROM bugs
            WHERE status IN (
                'Bugged',
                'Existing Bug',
                'Non-Recreatable',
                'QC Change',
                'New Req'
            )
            GROUP BY severity
            ORDER BY severity
            """
        )

        rows = cursor.fetchall()

        return {
            row["severity"]: row["count"]
            for row in rows
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Unable to retrieve bug summary"
        ) from exc

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()

@app.post("/bugs", status_code=201)
def create_bug(bug: dict):
    title = bug.get("title")
    severity = bug.get("severity")
    status = bug.get("status")

    if not title or not title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title is required"
        )

    if severity not in VALID_SEVERITIES:
        raise HTTPException(
            status_code=400,
            detail="Invalid severity"
        )

    if status not in VALID_STATUSES:
        raise HTTPException(
            status_code=400,
            detail="Invalid status"
        )

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        # The existing MySQL table does not use AUTO_INCREMENT.
        # Generate the next ID explicitly.
        cursor.execute(
            """
            SELECT COALESCE(MAX(id), 0) + 1 AS next_id
            FROM bugs
            """
        )

        next_id = cursor.fetchone()["next_id"]

        cursor.execute(
            """
            INSERT INTO bugs (
                id,
                title,
                severity,
                status
            )
            VALUES (%s, %s, %s, %s)
            """,
            (
                next_id,
                title.strip(),
                severity,
                status,
            ),
        )

        connection.commit()

        return {
            "id": next_id,
            "title": title.strip(),
            "severity": severity,
            "status": status,
        }

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()
