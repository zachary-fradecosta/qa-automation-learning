# 🚀 QA Automation Learning Journey

> A 90-day hands-on journey to become a QA Automation Engineer using Python, Pytest, Playwright and modern testing practices.

---

## 🎯 Project Goal

This repository documents my progression from manual QA to QA Automation.

Rather than following isolated tutorials, I am building a real automation framework step by step while learning the concepts used in professional QA teams.

The objective is to understand not only **how** to automate tests, but also **why** frameworks are designed this way.

---

## 🛠️ Tech Stack

Current

- Python
- JSON
- Pytest
- Pytest Fixtures
- Pytest Parametrization
- Pytest Markers
- Git
- GitHub
- API Testing

Coming soon

- Playwright
- GitHub Actions
- Page Object Model
- CI/CD
- Reporting

---

## 📂 Repository Structure

```text
qa-automation-learning/
│
├── day_01/                                     # Early Python learning exercises
├── day_02/
├── day_03/
│
├── data/
│   └── users.json                              # Test data
│
├── docs/
│   └── qa-automation-command-guide.md          # Commands Quick Guide
│
├── scripts/
│   └── day04_demo.py                           # Demo execution script
│
├── tests/
│   ├── conftest.py                             # Shared Pytest fixtures
│   ├── test_statistics.py
│   └── test_user_helpers.py
│
├── utils/
│   ├── json_loader.py
│   ├── statistics.py
│   └── user_helpers.py
│
├── .gitignore
├── pytest.ini                                  # Pytest configuration and markers
├── README.md
└── requirements.txt
```

⚠️ This temporary structure will evolve into a real automation framework during the learning journey.

---

## 📈 Progress

| Day | Topic | Status |
|-----|-------|--------|
| 1 | Python fundamentals | ✅ |
| 2 | Functions & filtering | ✅ |
| 3 | JSON & test data | ✅ |
| 4 | Modules & project architecture | ✅ |
| 5 | Python assertions and first unit tests | ✅ |
| 6 | Pytest - fixtures, conftest and parametrized tests | ✅ |
| 7 | Pytest fundamentals and automated test execution | ✅ |
| 8 | Pytest fixtures and parametrization | ✅ |
| 9 | Pytest markers and test suite selection | ✅ |
| 10 | Robust assertions and business rule validation | ✅ |
| 11 | Negative scenarios and edge cases | ✅ |
| 12 | Test data factories with Pytest fixtures | ✅ |
| 13 | API testing fundamentals with Requests | ✅ |
| 14 | [...] | ⏳ |

---

## 🎯 Final Goal

By the end of this journey, this repository will contain:

- UI Automation with Playwright
- API Testing
- Pytest
- Page Object Model
- Fixtures
- Reporting
- GitHub Actions
- Professional project structure

---

## 👨‍💻 About

This project is part of my journey to become a QA Automation Engineer.


---

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