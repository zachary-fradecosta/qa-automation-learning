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

### Day 15 — API Response Payload Validation

#### What I learned

- Verified that an API response returns the expected Python type.
- Checked mandatory fields in a JSON response.
- Validated field types such as `int` and `str`.
- Tested a list endpoint and verified the contract of every returned user.
- Distinguished fixed data expectations from rules that may evolve.

#### Key takeaway

A successful HTTP status code is not enough. API tests should also verify the structure, required fields and data types defined by the API contract.

---

### Day 16 — API POST Requests

#### What I learned

- Used `POST` to send JSON data to an API.
- Created a request payload with `title`, `body` and `userId`.
- Verified the `201 Created` response status.
- Checked that the API response contains the submitted data.
- Verified that the API creates an integer identifier.
- Understood the difference between a simulated creation and persistent data creation.

#### Key takeaway

A POST API test validates both the creation status and the response contract. The returned payload should contain the expected submitted values and a created resource identifier.

---

### Day 17 — API PUT and PATCH Requests

#### What I learned

- Used `PUT` to replace a complete API resource.
- Used `PATCH` to update only one field of a resource.
- Verified `200 OK` responses for update requests.
- Tested that an updated response contains the expected payload values.
- Understood why a partial update should use `PATCH` instead of an incomplete `PUT` request.

#### Key takeaway

PUT represents a full replacement of a resource, while PATCH updates only selected fields. Choosing the correct HTTP method protects data from unintended changes.

---

### Day 18 — API DELETE Requests

#### What I learned

- Used the `DELETE` HTTP method to request resource deletion.
- Created a DELETE request with `requests.delete()`.
- Learned that a successful deletion response can vary depending on the API contract.
- Validated the JSONPlaceholder DELETE response: `200 OK` and an empty JSON object.
- Added clear assertion messages to make API failures easier to diagnose.
- Executed the API test suite separately with the `api` marker.

#### Key takeaway

A successful DELETE request does not always return the same status code or response body. API tests must validate the documented contract of the API being tested.

---

### Day 19 — Reusable API Test Configuration

#### What I learned

- Used a Pytest fixture to centralize the API base URL.
- Built API URLs dynamically with f-strings.
- Removed duplicated API URLs from test files.
- Created a reusable POST payload fixture.
- Separated API configuration, test data, requests, and assertions.
- Verified the API suite independently and the complete test suite.

#### Key takeaway

Centralizing API configuration makes automated tests easier to maintain and safer to run across different environments.

---

### Day 20 — Reusable HTTP Sessions

#### What I learned

- Created a reusable `requests.Session()` fixture.
- Used `yield` in a Pytest fixture to prepare and clean up a resource.
- Closed the HTTP session with `session.close()` after each test.
- Replaced direct Requests calls with session methods.
- Applied the shared session to GET, POST, PUT, PATCH, and DELETE tests.
- Understood that an HTTP session does not select the target environment.

#### Key takeaway

A reusable HTTP session centralizes request configuration and prepares an API test suite for future authentication, headers, cookies, and shared connection settings.

---

### Day 21 — HTTP Headers and JSON API Contracts

#### What I learned

- Distinguished request headers from response headers.
- Configured the shared API session to request JSON responses.
- Used the `Accept` request header.
- Validated the `Content-Type` response header.
- Learned why `startswith("application/json")` is safer than an exact comparison.
- Verified HTTP headers in GET and POST API tests.

#### Key takeaway

HTTP status codes alone are not enough to validate an API response. A reliable API test also checks that the response format matches the expected contract.

---

### Day 22 — Safe API Environment Configuration

#### What I learned

- Created a dedicated API configuration module.
- Used `os.getenv()` to read the `QA_ENV` environment variable.
- Configured `test` as the safe default environment.
- Used a dictionary as a whitelist of approved environments.
- Raised a `ValueError` for an invalid environment.
- Used `monkeypatch` to test environment variables safely.
- Removed the hardcoded API URL from `conftest.py`.

#### Key takeaway

API tests should target only approved environments. A whitelist and an explicit error for unknown environments reduce the risk of running write requests against the wrong system.

---

### Day 23 — Mock API Testing

#### What I learned

- Created a reusable API client function.
- Learned the difference between live API tests and mocked API tests.
- Used the `requests_mock` Pytest fixture.
- Simulated HTTP `200`, `404`, and `500` responses.
- Tested API client behavior without calling an external API.
- Understood why mocked tests and live API tests are complementary.

#### Key takeaway

Mocked API tests are fast, deterministic, and useful for testing error scenarios. They cannot fully replace live API tests because they do not verify the real external service.

---

### Day 24 — HTTP Error Handling in the API Client

#### What I learned

- Used `response.raise_for_status()` in an API client.
- Changed the API client contract to return JSON data only for successful responses.
- Tested `404 Not Found` as an `HTTPError`.
- Tested `500 Internal Server Error` as an `HTTPError`.
- Verified the HTTP status attached to an exception.
- Understood why `None` is not precise enough for every API failure.

#### Key takeaway

An API client should return valid data for successful responses and raise explicit exceptions for HTTP failures. This prevents errors from being treated as valid business data.

---

### Day 25 — Configurable Timeouts and Network Failures

#### What I learned

- Added a configurable timeout to an API client function.
- Preserved a default timeout for existing client calls.
- Verified default and custom timeout values with `requests_mock`.
- Distinguished HTTP errors from network errors.
- Simulated `Timeout` and `ConnectionError` exceptions.
- Tested network failures without waiting for a real incident.

#### Key takeaway

An HTTP error means that a server returned an error response, while a timeout or connection error means that the client could not receive a usable response. These failures must remain distinguishable.


---

### Day 26 — API Query Parameters and Filtered Collections

#### What I learned

- Distinguished path parameters from query parameters.
- Used the Requests `params` argument to build a query string.
- Created an API client function to retrieve posts by user ID.
- Verified the query parameter actually sent by the client.
- Used `all()` to validate every item in a filtered collection.
- Distinguished an empty collection from a missing individual resource.

#### Key takeaway

A collection test must verify both the returned data and the filter sent in the request. A successful filtered request can legitimately return an empty list.

---

### Day 27 — API Pagination and Boundary Validation

#### What I learned

- Implemented pagination using `_page` and `_per_page` query parameters.
- Tested intermediate and partial final pages with mocked API responses.
- Verified the query parameters actually sent by the API client.
- Added client-side validation for page numbers and page sizes.
- Used parametrized tests to cover valid and invalid boundary values.
- Verified that invalid input is rejected before any HTTP request is sent.

#### Key takeaway

Pagination tests must distinguish the maximum page size from the actual number of returned items. A final page may contain fewer items without indicating an API defect. Validating pagination inputs before sending a request also prevents unnecessary and invalid network calls.

---

### Day 28 — Bearer Token Authentication

#### What I learned

- Added an authenticated API client method using a Bearer token.
- Sent an `Authorization` header with an API request.
- Inspected the headers actually sent by the client.
- Tested a successful authenticated response with `requests-mock`.
- Tested `401 Unauthorized` for an invalid token.
- Tested `403 Forbidden` for an authenticated user without sufficient permissions.
- Used fictional tokens to avoid exposing sensitive credentials.

#### Key takeaway

Authentication determines who the caller is, while authorization determines what the caller is allowed to do. A `401` response represents missing or invalid authentication, whereas a `403` response represents insufficient permissions for an authenticated caller.

---

### Day 29 — JSON Schema Validation

#### What I learned

- Created a reusable JSON Schema for an API profile response.
- Declared required properties and their expected JSON types.
- Rejected unexpected response properties with `additionalProperties`.
- Validated a successful API response with `jsonschema`.
- Tested missing required fields and invalid property types.
- Inspected `ValidationError.validator` to identify the broken contract rule.
- Learned that a successful HTTP status does not guarantee a valid response body.

#### Key takeaway

HTTP status validation and response contract validation cover different risks. An API can return `200 OK` while omitting a required field, changing a field type, or exposing an unexpected property. JSON Schema provides a reusable and centralized way to detect these contract regressions.

---

### Day 30 — Reusable API Client Class

#### What I learned

- Created a reusable `APIClient` class.
- Stored the HTTP session, base URL, and default timeout in an object.
- Centralized API URL construction.
- Normalized slashes between base URLs and endpoint paths.
- Created a generic `get()` method.
- Forwarded query parameters and headers to Requests.
- Supported default and request-specific timeouts.
- Tested successful responses, query parameters, timeouts, and HTTP errors.
- Preserved the existing functional API client methods during the refactoring.

#### Key takeaway

A reusable API client centralizes shared HTTP behavior and prevents every endpoint function from rebuilding URLs, forwarding configuration, and handling errors independently. Refactoring should remain progressive so that existing tests continue to protect the current behavior.


---

### Day 31 — API Client Fixture and Resource Methods

#### What I learned

- Created a shared `api_client` Pytest fixture.
- Injected an initialized API client directly into tests.
- Learned that fixtures from `conftest.py` must not be imported manually.
- Added specialized methods to the `APIClient` class.
- Reused the generic `get()` method instead of duplicating HTTP logic.
- Added methods for users, filtered posts, and authenticated profiles.
- Tested response data, query parameters, authorization headers, and HTTP errors.
- Continued migrating the API architecture without removing the existing functions.

#### Key takeaway

The generic client manages HTTP behavior, while specialized methods express business intent. Pytest fixtures centralize object creation and inject configured dependencies into tests without manual imports or repeated setup.

---

### Day 32 — API Architecture Chapter Review

#### What I practiced

- Migrated an existing schema test to the shared `api_client` fixture.
- Reviewed the complete request flow through the API framework.
- Reviewed HTTP methods, status codes, query parameters, sessions, and fixtures.
- Reviewed API mocking, network errors, timeouts, and pagination.
- Reviewed Bearer token authentication and authorization errors.
- Reviewed JSON Schema validation.
- Reviewed the separation between generic HTTP methods and specialized resource methods.

#### Chapter assessment

- QCM score: **14/15 — 93%**
- Chapter status: **Completed**
- Tests: **61 passed**
- API tests selected: **50**

#### Strengths

- HTTP methods and status codes
- Pytest fixtures and dependency injection
- API mocking
- HTTP and network error handling
- Pagination and query parameters
- JSON Schema validation
- Reusable API client architecture

#### Point to consolidate

Real credentials must be supplied through protected environment variables or CI secrets. They must never be committed to Git or exposed in documentation and logs.

#### Key takeaway

A maintainable API automation framework separates configuration, HTTP transport, resource-specific behavior, response contracts, and tests. Each layer has one responsibility and can be tested independently.

---

### Day 33 — First Playwright UI Tests

#### What I learned

- Installed Playwright and its Pytest plugin.
- Installed Chromium for browser automation.
- Used the Playwright `page` fixture.
- Navigated to a web page with `page.goto()`.
- Located elements by accessible role and name.
- Used web-first assertions to validate titles, headings, links, attributes, and URLs.
- Automated a user journey by clicking a link and validating the destination page.
- Learned why Playwright assertions are more reliable than fixed waits.

#### Key takeaway

Playwright can reproduce user interactions in a real browser and validate the resulting interface. Its accessible locators and automatically retried assertions make UI tests more reliable than scripts based on fixed waiting times.


---


