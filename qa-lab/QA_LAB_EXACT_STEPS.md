# QA Lab — Exact Build & Migration Steps

> **Project:** QA Bug API Lab  
> **Purpose:** Practical QA / backend / Linux / SQL / API / pytest / Git workflow  
> **Final architecture:** Windows/VS Code → Linux VM → FastAPI → MySQL → `qa_lab` → Postman → pytest → Linux logs/exit codes → Git  
> **Documentation scope:** Complete QA Lab build, migration, hardening, quality-gate work, and portfolio integration through October 5, 2026.

---

## 1. Original Lab

The original Windows project was:

```text
C:\Users\akash\my-freecodecamp-portfolio\qa-lab
```

Original files:

```text
app.py
database.py
requirements.txt
test_api.py
qa_lab.db
__pycache__/
```

The original API used:

- FastAPI
- SQLite
- pytest
- Postman

The original SQLite API had five tests, and the initial test suite passed:

```text
5 passed in 0.54s
```

### Initial QA review findings

The first review identified these weaknesses:

1. Whitespace-only bug titles were accepted.
2. `bug: dict` provided weak request validation.
3. Valid bug creation only checked the HTTP `201` response.
4. Summary testing only checked that the response was a dictionary containing P0/P1-style information.
5. Shared database state could leak between tests.

---

# 2. Linux / MySQL Lab Objective

The lab was expanded into this workflow:

```text
Windows / VS Code
       ↓
Linux VM
       ↓
FastAPI
       ↓
MySQL
       ↓
qa_lab
       ↓
Postman
       ↓
pytest
       ↓
Linux logs / exit codes
       ↓
Git
       ↓
AI review
```

The goal was to practice a realistic QA/backend workflow instead of only testing an isolated Python script.

---

# 3. Linux Environment

The Linux VM used:

```text
Python 3.12.3
MySQL 8.0.46
Ubuntu 24.04
```

The Linux workspace became:

```text
/home/sky/qa-lab
```

A Python virtual environment was created:

```bash
cd ~/qa-lab
python3 -m venv .venv
source .venv/bin/activate
```

---

# 4. Important Database Safety Rule

Existing MySQL databases:

```text
hitwicket_qa
racing_db
racing_game
qa_lab
```

### RULE

Only use:

```text
qa_lab
```

Do **not** modify:

```text
hitwicket_qa
racing_db
racing_game
```

---

# 5. Linux MySQL Root Access

Ubuntu MySQL used system authentication for root.

This worked:

```bash
sudo mysql -u root
```

This did not:

```bash
mysql -u root -p
```

It returned:

```text
ERROR 1698 (28000)
```

We did not change the root authentication configuration.

---

# 6. Verify the Existing QA Database

Inside MySQL:

```sql
SHOW DATABASES;
USE qa_lab;
SHOW TABLES;
DESCRIBE bugs;
SELECT COUNT(*) FROM bugs;
SELECT * FROM bugs LIMIT 5;
```

The database contained one table:

```text
bugs
```

The original row count was:

```text
44
```

---

# 7. Existing `bugs` Schema

The existing schema was preserved. We did not recreate or modify it.

```sql
CREATE TABLE bugs (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    severity TEXT NOT NULL,
    status TEXT NOT NULL,
    priority_by_qa TEXT,
    priority_by_product TEXT,
    dev_assigned TEXT
);
```

The MySQL description showed:

```text
id                  int       NOT NULL PRIMARY KEY
title               text      NOT NULL
severity            text      NOT NULL
status              text      NOT NULL
priority_by_qa      text      NULL
priority_by_product text      NULL
dev_assigned        text      NULL
```

Important discovery:

```text
id
```

was **not** configured as `AUTO_INCREMENT`.

That became relevant when implementing `POST /bugs`.

---

# 8. Initial Database Data

Initial severity counts:

```text
Medium    21
Low        7
High      12
Urgent     4
```

Initial status counts:

```text
Bugged                  12
Existing Bug            10
Non-Recreatable          2
Bug verified/QA Pass    14
QC Change                3
Bug fixed                1
New Req                  1
Not a bug                1
```

Open statuses used by the API:

```text
Bugged
Existing Bug
Non-Recreatable
QC Change
New Req
```

Initial open count:

```text
28
```

Developer counts:

```text
Akash          21
Bishal         11
Kunal           9
Akash Deep      2
Arsalaan        1
```

---

# 9. Create a Restricted MySQL Application User

The application should not use MySQL root.

The intended application user was:

```text
qa_app
```

The first attempted password was rejected by MySQL password policy.

A stronger password was temporarily used while creating the account, after which the lab password was configured.

The final account was recreated cleanly with only the required database privileges.

```sql
DROP USER 'qa_app'@'localhost';

CREATE USER 'qa_app'@'localhost'
IDENTIFIED BY '<LAB_DB_PASSWORD>';

GRANT SELECT, INSERT, UPDATE, DELETE
ON qa_lab.*
TO 'qa_app'@'localhost';
```

> The actual password is intentionally not stored in this documentation or Git.

Final privileges were verified as:

```text
GRANT USAGE ON *.* TO `qa_app`@`localhost`
GRANT SELECT, INSERT, UPDATE, DELETE ON `qa_lab`.* TO `qa_app`@`localhost`
```

The account was tested successfully.

Access to the protected database was denied as expected:

```sql
USE hitwicket_qa;
```

---

# 10. Linux Application Environment

Environment variables were used instead of putting database credentials directly into Python:

```bash
export DB_HOST="127.0.0.1"
export DB_USER="qa_app"
export DB_PASSWORD="<LAB_DB_PASSWORD>"
export DB_NAME="qa_lab"
```

Do not commit these values to Git.

Do not put the database password into:

- source code
- README files
- screenshots
- Git history
- `.env` files committed to Git

---

# 11. Copy the Application to Linux

The application files copied from Windows/shared storage to Linux were:

```text
app.py
database.py
requirements.txt
test_api.py
```

The SQLite database was deliberately **not** copied as the application database because the Linux version uses the existing MySQL `qa_lab` database.

Files copied into:

```text
/home/sky/qa-lab
```

Root ownership from the shared-folder copy was fixed with:

```bash
sudo chown sky:sky app.py database.py requirements.txt test_api.py
```

---

# 12. Python MySQL Driver

The original application used:

```python
sqlite3
```

The Linux version uses:

```text
mysql-connector-python
```

It was installed in the Linux virtual environment.

---

# 13. Final `database.py`

The final database module became:

```python
import os

import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
    )


def initialize_database():
    # The qa_lab.bugs table already exists.
    # Do not recreate or modify the existing schema.
    pass
```

### Important design decision

The API does not create or modify the existing `bugs` table.

The lab uses the pre-existing schema as a test target.

---

# 14. Database Connection Test

Connection was tested with:

```bash
python -c "from database import get_connection; c=get_connection(); print(c.is_connected()); c.close()"
```

Result:

```text
True
```

---

# 15. Final FastAPI Application

The final `app.py` contains:

- health check
- GET all bugs
- bug summary
- POST bug
- severity validation
- status validation
- title validation
- MySQL transactions
- rollback on failure
- connection cleanup

The important validation sets are:

```python
VALID_SEVERITIES = {
    "Low",
    "Medium",
    "High",
    "Urgent",
}
```

```python
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
```

Open statuses:

```python
OPEN_STATUSES = {
    "Bugged",
    "Existing Bug",
    "Non-Recreatable",
    "QC Change",
    "New Req",
}
```

The health endpoint returns:

```json
{
  "status": "QA Bug API is running"
}
```

---

# 16. Important `POST /bugs` Database Discovery

The first Linux implementation attempted to insert a bug without explicitly supplying an ID.

The request failed with:

```text
mysql.connector.errors.DatabaseError:
1364 (HY000): Field 'id' doesn't have a default value
```

Cause:

```text
bugs.id
```

was not `AUTO_INCREMENT`.

### We did NOT modify the schema.

Instead, for this controlled single-process lab, the API generates the next ID:

```sql
SELECT COALESCE(MAX(id), 0) + 1 AS next_id
FROM bugs
```

The resulting ID is then inserted explicitly.

### Important limitation

`MAX(id) + 1` is acceptable for this controlled lab but is **not concurrency-safe production design**.

A production system should use an appropriate database-generated identity/sequence mechanism.

---

# 17. Syntax Validation

Python syntax was checked with:

```bash
python -m py_compile app.py database.py
```

No output indicated successful compilation.

---

# 18. FastAPI / Uvicorn

The application was run with:

```bash
python -m uvicorn app:app --host 0.0.0.0 --port 8000
```

---

# 19. Manual API Verification

Health check:

```text
GET /
```

Returned:

```json
{
  "status": "QA Bug API is running"
}
```

Bug listing:

```text
GET /bugs
```

Returned the real MySQL bug records.

---

# 20. Successful Bug Creation

After fixing the ID-generation issue:

```text
POST /bugs
```

was successfully tested with:

```json
{
  "title": "Linux MySQL integration test bug",
  "severity": "Low",
  "status": "Bugged"
}
```

Response:

```json
{
  "id": 45,
  "title": "Linux MySQL integration test bug",
  "severity": "Low",
  "status": "Bugged"
}
```

The inserted row was independently verified in MySQL:

```sql
SELECT id, title, severity, status
FROM qa_lab.bugs
WHERE id = 45;
```

The API's `GET /bugs` also returned the new record.

---

# 21. Bug Summary Endpoint

The endpoint:

```text
GET /bugs/summary
```

counts bugs whose status is in the open-status set.

After inserting the test bug, the result was:

```json
{
  "High": 5,
  "Low": 8,
  "Medium": 16
}
```

The Low count increased from 7 to 8 because the new test bug was:

```text
Low + Bugged
```

---

# 22. Postman Testing

Manual API testing was performed with Postman.

Tests included:

### Valid POST

Verified:

```text
201 Created
```

and the returned bug data.

### GET bugs

Verified the real database data was returned.

### Invalid severity

Example:

```text
P7
```

Expected:

```text
400
```

### GET summary

Verified the summary endpoint returned the expected open-bug severity information.

---

# 23. Improved Automated Test Suite

The original test file was replaced with a stronger test suite.

The final suite contains:

```text
test_health_check
test_get_bugs
test_create_valid_bug
test_invalid_severity
test_invalid_status
test_missing_title
test_empty_title
test_summary
```

Total:

```text
8 tests
```

---

# 24. Valid Creation Test

The valid creation test verifies:

- HTTP status is `201`
- title matches
- severity matches
- status matches
- returned ID is an integer

The created test row is then deleted from MySQL so the test does not permanently pollute the database.

---

# 25. Negative Testing

Invalid severity:

```text
P7
```

Expected:

```text
400
Invalid severity
```

Invalid status:

```text
Open
```

Expected:

```text
400
Invalid status
```

Missing title:

Expected:

```text
400
Title is required
```

Whitespace-only title:

```text
"   "
```

Expected:

```text
400
Title is required
```

This specifically addressed the weakness found during the earlier AI review.

---

# 26. Summary Test

The summary test verifies:

- HTTP `200`
- response is a dictionary
- `High` exists
- `Low` exists
- `Medium` exists
- expected High count
- expected Medium count
- Low count is at least the expected value

The final known values were:

```text
High   = 5
Medium = 16
Low    >= 8
```

---

# 27. Pytest Environment Issues

Pytest was initially missing.

It was installed.

The FastAPI `TestClient` also required the HTTP client dependency, so `httpx` was installed.

An initial pytest run failed because the shell did not have the database environment variables.

The environment was then exported correctly.

A second connection issue was caused by an incorrect `DB_PASSWORD` environment value.

The interactive MySQL login worked, the environment value was corrected, and the Python connection test returned:

```text
True
```

---

# 28. Final Pytest Result

The final test command:

```bash
pytest -v
```

returned:

```text
8 passed, 1 warning in 0.62s
```

The warning was a Starlette/AnyIO deprecation warning and did not cause a test failure.

Final tests:

```text
test_health_check       PASSED
test_get_bugs           PASSED
test_create_valid_bug   PASSED
test_invalid_severity   PASSED
test_invalid_status     PASSED
test_missing_title      PASSED
test_empty_title        PASSED
test_summary            PASSED
```

---

# 29. Final Requirements

The final `requirements.txt` was updated to contain the dependencies actually used by the lab:

```text
fastapi
uvicorn
mysql-connector-python
pytest
httpx
```

---

# 30. Git Problem We Discovered

The main portfolio repository is:

```text
C:\Users\akash\my-freecodecamp-portfolio
```

It uses:

```text
main
```

and is connected to:

```text
origin/main
```

Initially, `qa-lab` was itself a separate Git repository:

```text
my-freecodecamp-portfolio/
└── qa-lab/
    └── .git/
```

The `qa-lab` repository had:

```text
ec86459 Build QA bug API lab
a462857 Build QA bug API
```

It had no remote:

```bash
git remote -v
```

returned nothing.

The parent portfolio repository tracked `qa-lab` as a Gitlink:

```text
160000 ec8645934b104a7c921290e5036e9f9f120d4251 0 qa-lab
```

There was also no valid `.gitmodules` mapping.

---

# 31. Converting QA Lab into the Main Portfolio Repository

The parent repository was clean before making the change.

The Gitlink was removed from the parent index:

```bash
git rm --cached qa-lab
```

This left:

```text
D  qa-lab
?? qa-lab/
```

The nested Git repository was then removed:

```bash
rm -rf qa-lab/.git
```

This removed only the nested Git metadata.

The actual project files remained.

---

# 32. Final QA Lab `.gitignore`

The final `.gitignore` is:

```text
qa_lab.db
__pycache__/
.pytest_cache/
*.pyc
.env
.venv/
```

This prevents local database/cache/environment files from entering the main repository.

The SQLite file:

```text
qa_lab.db
```

is intentionally excluded because the final Linux lab uses MySQL.

---

# 33. Staging the Real Project

After removing the Gitlink and nested `.git`, the parent repository detected:

```text
qa-lab/.gitignore
qa-lab/README.md
qa-lab/app.py
qa-lab/database.py
qa-lab/requirements.txt
qa-lab/test_api.py
```

It did not detect:

```text
qa_lab.db
__pycache__/
.pytest_cache/
```

because of `.gitignore`.

The project was staged:

```bash
git add qa-lab
```

---

# 34. Final Git Commit

The staged change was committed with:

```bash
git commit -m "Integrate QA lab into portfolio"
```

Commit created:

```text
56cc257
```

Commit message:

```text
Integrate QA lab into portfolio
```

Git reported:

```text
7 files changed, 187 insertions(+), 1 deletion(-)
```

The old Gitlink was deleted and the real QA lab files were created in the parent repository.

---

# 35. Final Git Push

The commit was pushed with:

```bash
git push origin main
```

Push result:

```text
efc5fe4..56cc257  main -> main
```

The final verification:

```bash
git status
```

returned:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

---

# 36. Final Repository Structure

The QA lab is now a normal project inside the master FreeCodeCamp portfolio repository:

```text
my-freecodecamp-portfolio/
│
├── _config.yml
├── README.md
├── py-algorithms/
├── py-algorithns/
├── python-projects/
│
└── qa-lab/
    ├── .gitignore
    ├── README.md
    ├── app.py
    ├── database.py
    ├── requirements.txt
    └── test_api.py
```

Local-only files intentionally excluded:

```text
qa_lab.db
__pycache__/
.pytest_cache/
.venv/
.env
```

---

# 37. What This Lab Demonstrated

This was more than a FastAPI exercise.

The completed workflow covered:

```text
Python
   ↓
FastAPI
   ↓
Linux
   ↓
MySQL
   ↓
Database permissions
   ↓
Environment variables
   ↓
REST API
   ↓
Postman
   ↓
Positive testing
   ↓
Negative testing
   ↓
pytest automation
   ↓
Database verification
   ↓
Transactions / rollback
   ↓
Linux process execution
   ↓
Exit codes / logs
   ↓
Git
   ↓
GitHub
   ↓
AI-assisted QA review
```

The lab also exposed realistic engineering problems rather than hiding them:

- MySQL authentication differences
- password policy
- excessive database privileges
- missing environment variables
- wrong database credentials
- missing Python dependencies
- missing `httpx`
- schema constraints
- non-auto-increment IDs
- test data cleanup
- shared test state
- Git submodule/gitlink confusion
- repository migration
- ignored local artifacts

---

# 38. Important Lessons

## Database permissions

Applications should not run as database root.

Use a restricted account with only the permissions required by the application.

## Environment configuration

Secrets should come from environment variables rather than source code.

## Existing schemas

Before changing a database, inspect:

```sql
SHOW TABLES;
DESCRIBE table_name;
SELECT COUNT(*) FROM table_name;
```

Understand the existing system before modifying it.

## API testing

A successful status code is not enough.

Test:

```text
input
→ expected behavior
→ actual response
→ database state
```

## Negative testing

Invalid inputs are first-class test cases.

## Automated testing

A good API test can verify both:

```text
HTTP response
```

and:

```text
database state
```

## Git

Always inspect:

```bash
git status
git diff
git diff --cached
```

before committing.

## Git repositories

A nested `.git` directory changes how Git treats a directory. A Gitlink/submodule-style entry is different from ordinary tracked files.

---

# 39. Current Known State

As of the final push:

```text
Repository:
my-freecodecamp-portfolio

Branch:
main

Latest lab integration commit:
56cc257

Remote:
origin/main

Working tree:
clean

QA test result:
8 passed, 1 warning

Database:
MySQL qa_lab

API:
FastAPI

Test automation:
pytest

Manual API testing:
Postman
```

---

# 40. Future Lab Improvements

These are not completed in this documented lab and should be treated as future work rather than completed functionality:

1. Replace `bug: dict` with a proper Pydantic request model.
2. Add stronger response validation.
3. Improve database-generated IDs for concurrency-safe production behavior.
4. Improve test isolation using fixtures/transactions or a dedicated test database.
5. Add API tests for malformed request bodies.
6. Add tests for all valid severities and statuses.
7. Add CI/CD execution through GitHub Actions.
8. Add Linux shell automation around the test suite.
9. Add structured application logging.
10. Add API contract testing.
11. Add more database-level assertions.
12. Add AI-assisted test generation and test review as a controlled workflow.

---

# 41. Lab Completion Checkpoint

The lab's completed checkpoint is:

```text
Windows
  ↓
Linux VM
  ↓
FastAPI
  ↓
MySQL
  ↓
qa_lab
  ↓
Postman
  ↓
pytest
  ↓
8 passing tests
  ↓
Git
  ↓
GitHub
```

The QA Lab is now integrated into the master FreeCodeCamp portfolio repository and the working tree is clean.


---

# 42. October 5, 2026 — Weekend Quality-Gate Lab

This checkpoint extended the existing `qa_lab` rather than creating a new project, framework, or database.

Objective:

```text
Specification
→ SQL ground truth
→ bounded implementation
→ deterministic tests
→ Linux quality gate
→ real HTTP verification
→ AI evaluation
→ human approval
→ portfolio documentation
```

## 42.1 Specification

Target endpoint:

```text
GET /bugs/summary
```

Contract:

- no request body
- no query parameters
- return open-bug counts grouped by severity
- counts are integers
- only the defined open statuses are included
- closed/non-open statuses are excluded
- no matching rows return `{}`
- database/runtime failures must not silently become an empty successful response
- existing endpoints remain unaffected
- no schema, dependency, authentication, or unrelated-code changes

Open statuses:

```text
Bugged
Existing Bug
Non-Recreatable
QC Change
New Req
```

The normative API contract is maintained in `SUMMARY_API_SPEC.md`.

## 42.2 SQL Ground Truth

Independent MySQL verification used:

```sql
SELECT
    severity,
    COUNT(*)
FROM bugs
WHERE status IN (
    'Bugged',
    'Existing Bug',
    'Non-Recreatable',
    'QC Change',
    'New Req'
)
GROUP BY severity;
```

Ground truth:

```text
High   = 5
Low    = 9
Medium = 16
```

Total open bugs:

```text
30
```

## 42.3 Bounded Implementation

The change was deliberately limited to the existing lab.

Allowed files:

```text
app.py
test_api.py
database.py only if strictly required
```

Constraints:

- smallest practical change
- preserve SQL and response contract
- no schema changes
- no new dependencies
- no unrelated endpoint changes
- no persistent test data
- no credential changes

`GET /bugs/summary` was hardened with explicit connection/cursor cleanup and controlled HTTP 500 behavior for unexpected runtime/database failures. The SQL itself was preserved.

For this controlled lab, the broad exception boundary is acceptable. Production code should normally catch specific database/runtime exceptions where appropriate.

## 42.4 Deterministic Testing

The summary test was strengthened to assert the exact response:

```json
{
    "High": 5,
    "Low": 9,
    "Medium": 16
}
```

It also verifies integer values.

Additional tests verify:

### Closed-status exclusion

A temporary `Urgent` / `Bug fixed` row was inserted, the endpoint was called, and `Urgent` was confirmed absent. The row was cleaned up and independently verified to be absent afterward.

### Empty result

A deterministic `monkeypatch` fake database result verifies:

```json
{}
```

without modifying the real MySQL database.

## 42.5 Quality Gate

Final Linux test result:

```text
10 passed, 1 warning
```

The warning was an unrelated Starlette/AnyIO deprecation warning.

Python compilation was also verified with:

```bash
python -m compileall app.py test_api.py database.py
```

No compilation errors were reported.

Real HTTP verification through Uvicorn and curl returned:

```json
{"High":5,"Low":9,"Medium":16}
```

This matched the independent SQL result.

## 42.6 AI Evaluation

The completed implementation was evaluated against the agreed specification without further modification.

Result:

```text
12 / 12 criteria PASS
```

Criteria included exact counts, integer values, open-status filtering, empty-result behavior, schema preservation, regression coverage, response-contract preservation, failure handling, dependency preservation, test-data cleanup, compilation, and real HTTP/SQL agreement.

## 42.7 Human Approval

Final approval checkpoint:

```text
SPECIFICATION       PASS
IMPLEMENTATION      PASS
DETERMINISTIC TESTS PASS
QUALITY GATE        PASS
AI EVALUATION       12/12 PASS
HUMAN APPROVAL      APPROVED
```

---

# 43. October 5, 2026 — Windows Portfolio Integration

Linux remains the execution/testing environment.

Windows remains the source-control and portfolio environment:

```text
C:\Users\akash\my-freecodecamp-portfolio
```

Only the verified changed files were exported from Linux:

```text
app.py
test_api.py
```

They were transferred through the existing VirtualBox Windows Downloads shared folder and copied into `qa-lab`.

The documentation is being updated on Windows so the final development record is committed with the code.

No blind `git add .` workflow is being used.

---

# 44. Week Progress — Engineering Learning

This week's progression moved from making an API work toward running a complete quality-gate workflow:

```text
API implementation
→ database integration
→ SQL ground truth
→ specification
→ bounded change
→ deterministic testing
→ real HTTP verification
→ AI evaluation
→ human approval
→ portfolio documentation
```

Key concepts reinforced:

- Python functions and exception handling
- FastAPI route behavior
- MySQL connectivity
- SQL filtering and aggregation
- `WHERE` and grouped aggregation
- API response contracts
- positive and negative testing
- deterministic tests
- test isolation and cleanup
- monkeypatching
- Linux virtual environments
- real HTTP vs in-process `TestClient`
- Git scope control
- least-privilege database access
- separation of concerns
- reproducibility
- AI-assisted engineering review

The important capability shift is:

```text
"write code → see if it works"
```

to:

```text
specification
→ implementation
→ deterministic evidence
→ independent verification
→ quality gate
→ review
→ approval
→ documented portfolio change
```

---

# 45. Current Checkpoint — October 5, 2026

```text
Specification             100%
SQL ground truth          100%
Pre-change inspection     100%
Bounded implementation    100%
Deterministic tests       100%
Linux quality gate       100%
Real HTTP verification    100%
AI evaluation             100%
Human approval            100%
Windows export            100%
Documentation update      100%
Windows Git verification    NEXT
Git commit + push           NEXT
```

Current lab completion before final Windows Git operations:

```text
~95%
```

Remaining:

```text
Windows git diff
→ final checks
→ git diff --check
→ stage intended files only
→ commit
→ push
→ verify clean working tree
```

---

# 46. Next Engineering Improvements

The existing future-work list remains valid:

1. Replace `bug: dict` with a Pydantic request model.
2. Add stronger API response validation.
3. Improve test isolation with fixtures/transactions or a dedicated test database.
4. Add malformed-request tests.
5. Improve concurrency-safe ID generation.
6. Add CI execution through GitHub Actions.
7. Add Linux shell automation around the quality gate.
8. Add structured application logging.
9. Add API contract testing.
10. Build a small deterministic evaluator comparing expected API behavior with test results.

These remain future improvements unless explicitly completed later.
