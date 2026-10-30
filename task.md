# Task: Fix Duplicate Employee Results in a FastAPI Endpoint

## Topology

PyCharm (LOOKUP) → Terminal.app (LOOKUP) → Postman (LOOKUP) → PyCharm (MODIFY) → Terminal.app (LOOKUP) → Postman (LOOKUP)

## Request

### 1. Domain / Role

Software Development — Python Backend Developer specializing in REST APIs, debugging, and database operations.

### 2. Goal

Fix a bug in a Python REST API that retrieves employee records but produces duplicate results under certain filtering conditions and handles invalid input incorrectly.

The objective is to identify the root cause, correct the retrieval logic, implement appropriate input validation, and verify that the API returns the expected results for representative requests.

### 3. Starting Materials

A small existing Python project containing:

- A FastAPI application with one or two endpoints.
- A simple employee data model backed by a lightweight SQLite database.
- An endpoint that retrieves and filters employee records.
- An existing bug affecting record retrieval or filtering.
- A few sample API requests demonstrating the incorrect behavior.

The project will use synthetic employee data, run locally, and require no external services or complex infrastructure.

### 4. Steps (with the apps for each)

#### Step 1: Reproduce the bug

- Open the existing project and run the application locally.
- Send a request that demonstrates the incorrect retrieval behavior.
- Inspect the relevant endpoint and identify the cause of the issue.

**Apps:** PyCharm, Terminal, and Postman

#### Step 2: Fix the retrieval and input handling

- Correct the filtering or retrieval logic to prevent unintended duplicate results.
- Add appropriate validation for invalid input.
- Implement suitable error handling while preserving the existing API behavior.

**Apps:** PyCharm and Terminal

#### Step 3: Verify the fix

- Repeat the original request to confirm that the bug is resolved.
- Test a valid request, an invalid input, and a request with no matching employee records.
- Check the returned records, HTTP status codes, and error responses.

**Apps:** PyCharm, Terminal, and Postman

> The recorded workflow will focus exclusively on reproducing the bug, implementing the necessary fix, and verifying the key scenarios. Broader testing, additional documentation, and optional improvements will remain outside the recording.

### 5. Deliverable

A working FastAPI endpoint with corrected employee retrieval logic, appropriate input validation, and proper error handling.

The final result will include the modified Python code and a demonstration of the fix through representative API requests.

### Apps

| App | Purpose |
|---|---|
| PyCharm | Inspect and modify the Python code |
| Terminal | Run the application and execute commands |
| Postman | Reproduce the issue and verify API responses |

## Task Description

1. Run the existing API and reproduce the duplicate employee results.
2. Inspect the endpoint and fix the retrieval logic and input handling.
3. Restart the updated application.
4. Verify the original request and the valid, invalid, and no-match cases.
