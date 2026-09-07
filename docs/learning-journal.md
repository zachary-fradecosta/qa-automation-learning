## 📓 Learning Journal

### Day 1 — Python Fundamentals

#### What I learned

- Worked with variables, basic data types, booleans, lists and dictionaries.
- Used loops and conditions to process user data.
- Created simple functions to organize Python logic.
- Started manipulating a realistic list of users for QA scenarios.

#### Key takeaway

Python fundamentals are the foundation of test automation. Test data is often represented with lists and dictionaries, so being able to read and manipulate them is essential.

---

### Day 2 — Functions and User Filtering

#### What I learned

- Created reusable functions to filter active users.
- Searched for users by username.
- Filtered users by role.
- Validated required user fields such as username and password.
- Created eligibility logic based on multiple business rules.
- Calculated user statistics.

#### Key takeaway

A QA Automation Engineer must translate business rules into clear and reusable functions that can later be covered by automated tests.

---

### Day 3 — JSON and Test Data

#### What I learned

- Loaded user data from a JSON file.
- Separated test data from Python logic.
- Created a reusable function to load JSON files.
- Identified users with missing passwords.

#### Key takeaway

Keeping test data outside the code makes tests easier to read, update and maintain.

---

### Day 4 — Python Modules and Project Architecture

#### What I learned

- Created reusable Python modules.
- Organized the project into packages.
- Imported functions instead of duplicating code.
- Separated test data, reusable logic and execution scripts.
- Understood how Python resolves imports.
- Troubleshot `ModuleNotFoundError` and `FileNotFoundError`.

#### Key takeaway

Reusable functions should exist in one location and be imported wherever they are needed. Separating responsibilities makes a test automation project easier to maintain.

---

### Day 5 — Python Assertions and First Unit Tests

#### What I learned

- Used Python assertions to verify expected behavior.
- Wrote first unit tests for user helper functions.
- Practiced the Arrange, Act and Assert structure.
- Tested valid and invalid user data.
- Tested expected and unexpected user search results.

#### Key takeaway

An assertion turns an expected business behavior into a verifiable automated check. A good test protects the expected behavior against regressions.

---

### Day 6 — Test Consolidation & Transition to Pytest

#### What I learned

- Consolidated the use of Python `assert` statements for testing.
- Practiced the **Arrange → Act → Assert (AAA)** testing pattern.
- Learned why tests should be independent from each other.
- Practiced testing both expected and edge-case behaviors.
- Learned how automated tests can detect regressions after code changes.
- Practiced deliberately breaking code to verify that tests correctly detect failures.
- Prepared the project for the transition to Pytest.

#### Key takeaway

Good automated tests do more than verify that the code works. They protect expected behavior and help detect regressions when the code or test data changes.


---

### Day 7 — Pytest Fundamentals

#### What I learned

- Installed and configured Pytest.
- Learned how Pytest discovers and executes tests automatically.
- Replaced manual test execution with Pytest.
- Learned how to interpret passed and failed tests.
- Practiced writing independent test cases.
- Learned how to execute individual tests with Pytest.

#### Key takeaway

Pytest automates the execution of test functions and provides a clear report when an assertion fails. Automated tests allow regressions to be detected without manually checking the application.

---

### Day 8 — Pytest Fixtures and Parametrization

#### What I learned

- Understood how Pytest fixtures prepare reusable test data.
- Used a shared fixture to load users from a JSON file.
- Learned how Pytest injects fixtures into tests.
- Used parametrization to run the same test with multiple data sets.
- Removed duplicate test cases while preserving test coverage.

#### Key takeaway

Fixtures prepare reusable test context, while parametrization executes the same behavior with multiple scenarios. Both techniques make an automated test suite more readable and maintainable.

---

### Day 9 — Pytest Markers

#### What I learned

- Created a `pytest.ini` configuration file.
- Declared custom Pytest markers.
- Categorized tests as `smoke` and `regression`.
- Executed selected test groups with `pytest -m`.
- Combined and excluded markers using Pytest expressions.

#### Key takeaway

Markers organize a test suite according to testing goals. They allow critical smoke checks and broader regression checks to run independently in local development or CI/CD pipelines.

---

### Day 10 — Robust Assertions

#### What I learned

- Used `all()` to validate a rule for every returned item.
- Distinguished fixed test-data expectations from business rules.
- Added meaningful assertion messages.
- Strengthened tests for active and eligible users.

#### Key takeaway

A robust test verifies business behavior rather than duplicating the implementation. Multiple assertions are appropriate when they validate different aspects of one behavior.

---

### Day 11 — Negative Scenarios and Edge Cases

#### What I learned

- Created tests for situations where no result is expected.
- Tested an empty user list.
- Verified that no eligible users are returned when all users fail the eligibility rules.
- Used local test data for test-specific scenarios.

#### Key takeaway

Negative tests verify that the application handles invalid, empty or non-matching data correctly. They are essential for preventing regressions in edge cases.

---

### Day 12 — Test Data Factories

#### What I learned

- Created a reusable `user_factory` fixture.
- Generated custom user data directly inside a test.
- Used a factory fixture to avoid repeating user dictionary structures.
- Distinguished fixed JSON data from flexible test-specific data.
- Learned that Pytest only discovers fixtures after the fixture file is saved.

#### Key takeaway

A factory fixture creates flexible and readable test data. It is useful when several scenarios need similar objects with different values.

---

### Day 13 — API Testing Fundamentals

#### What I learned

- Installed and used the `requests` library.
- Sent a `GET` request to a public API endpoint.
- Read HTTP status codes.
- Converted an API JSON response into a Python dictionary.
- Created a first API test with Pytest.
- Configured Python to use system certificates for HTTPS requests.

#### Key takeaway

API testing verifies the contract between a client and a service. A reliable API test checks the HTTP response and the expected JSON data.

---

### Day 14 — API Error Responses and API Markers

#### What I learned

- Added an `api` marker to categorize API tests.
- Executed only API tests with `pytest -m api`.
- Tested a successful API response with HTTP `200`.
- Tested an unknown API resource with HTTP `404`.
- Distinguished an expected client error from an unexpected server error.

#### Key takeaway

An HTTP error response can be an expected API behavior. A test should validate the response code defined by the API contract, such as `404` for a resource that does not exist.

---