# GET /bugs/summary Specification

## Endpoint

GET /bugs/summary

## Input

No request body.

No query parameters.

## Output

Return a JSON object containing the number of open bugs grouped by severity.

Example:

    {
      "High": 5,
      "Low": 9,
      "Medium": 16
    }

## Open statuses

The following statuses are considered open:

- Bugged
- Existing Bug
- Non-Recreatable
- QC Change
- New Req

Statuses outside this list are excluded from the summary.

## Aggregation

Count bugs by severity after filtering to open statuses.

Conceptually:

    SELECT severity, COUNT(*)
    FROM bugs
    WHERE status IN (
        'Bugged',
        'Existing Bug',
        'Non-Recreatable',
        'QC Change',
        'New Req'
    )
    GROUP BY severity;

## Empty database

If there are no bugs matching the open-status criteria, the API should return:

    {}

## Invalid data

The API should not silently invent or alter invalid database values.

If unexpected severity/status data exists in the database, the behavior must be verified against the actual database state and implementation.

## Acceptance Criteria

- GET /bugs/summary returns HTTP 200 for valid database access.
- Only bugs with open statuses are included.
- Results are grouped by severity.
- Each severity value contains the correct count.
- Closed/non-open statuses are excluded.
- An empty set of matching bugs returns {}.
- The API result must agree with the corresponding SQL aggregation.
- Automated tests must verify exact expected counts.
- API behavior must be verified independently with curl or Postman.
- The final implementation must pass the complete pytest suite.

---

## Implementation / Verification Status — October 5, 2026

This specification was used as the acceptance contract for the October 5, 2026 quality-gate lab.

Verified database result:

```text
High   = 5
Low    = 9
Medium = 16
```

Verification:

```text
pytest
→ 10 passed, 1 warning

real HTTP / curl
→ {"High":5,"Low":9,"Medium":16}

AI evaluation
→ 12/12 criteria PASS

Human approval
→ APPROVED
```

Additional deterministic coverage verifies closed-status exclusion, empty-result behavior, integer response values, and cleanup of temporary test data.

The SQL aggregation itself was preserved during the hardening change.
