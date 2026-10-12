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
│   └── users.json                              # Local test data
│
├── docs/                                       # QA Automation reference guides
│   ├── api-requests.md
│   ├── api-response-validation.md
│   ├── api-test-architecture.md
│   ├── git-and-github.md
│   ├── learning-journal.md
│   ├── pytest.md
│   └── python-project.md
│
├── schemas/
│   ├── __init__.py
│   └── profile_schema.py                     # JSON Schema for profile responses
│
├── scripts/                                    # Standalone learning demonstrations
│   ├── day04_demo.py
│   ├── api_client.py                            # Reusable API client functions
│   ├── api_demo.py
│   ├── api_post_demo.py
│   ├── api_put_demo.py
│   └── api_delete_demo.py
│
├── tests/                                      # Automated test suite
│   ├── conftest.py                             # Shared Pytest fixtures
│   ├── test_api_client.py                      # Mocked API client tests
│   ├── test_api_config.py                      # API environment configuration tests
│   ├── test_api_posts.py
│   ├── test_api_session.py                     
│   ├── test_api_users.py
│   ├── test_statistics.py
│   └── test_user_helpers.py
│
├── utils/                                      # Application helper functions
│   ├── api_config.py                           # Safe API environment configuration
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

## Documentation

The `docs/` folder contains practical reference guides for the technologies and commands used in this project.

- [API Requests Guide](docs/api-requests.md): HTTP methods, endpoints, payloads, and status codes.
- [API Response Validation Guide](docs/api-response-validation.md): JSON validation, required fields, types, and HTTP headers.
- [API Test Architecture Guide](docs/api-test-architecture.md): Fixtures, sessions, reusable API configuration, and safe environments.
- [Pytest Guide](docs/pytest.md): Test execution, markers, and Pytest commands.
- [Git and GitHub Guide](docs/git-and-github.md): Git workflow and GitHub commands.
- [Python Project Guide](docs/python-project.md): Useful Python project commands.
- [Learning Journal](docs/learning-journal.md): Daily learning notes, key takeaways, exercises, and progress.

These guides are updated as new tools and QA Automation concepts are learned.

---

## 📈 Learning Progress

| Chapter | Days | Main Topics | Status |
|---|---:|---|---|
| 1. Python and QA Foundations | 1–6 | Python basics, functions, JSON, modules, assertions and QA thinking | ✅ Completed |
| 2. Pytest Fundamentals | 7–12 | Test discovery, fixtures, parametrization, markers, negative testing and factories | ✅ Completed |
| 3. API Testing Fundamentals | 13–18 | GET, POST, PUT, PATCH, DELETE and response validation | ✅ Completed |
| 4. API Test Architecture | 19–32 | Sessions, configuration, environments, mocks, error handling, timeouts, filtering, pagination and authentication | 🔄 In progress |
| 5. Playwright Fundamentals | 33–42 | Browser automation, locators, actions, assertions and waiting strategies | ⏳ Planned |
| 6. UI Test Architecture | 43–52 | Pytest fixtures, test data, Page Object Model and reusable components | ⏳ Planned |
| 7. Advanced Playwright | 53–59 | Multiple pages, frames, downloads, uploads, network mocking and cross-browser testing | ⏳ Planned |
| 8. API and UI Integration | 60–64 | API-based setup, UI verification and end-to-end workflows | ⏳ Planned |
| 9. Test Reporting | 65–69 | HTML reports, Allure, screenshots, traces and test artifacts | ⏳ Planned |
| 10. SQL for QA Automation | 70–75 | Queries, filters, joins, aggregations and database validation | ⏳ Planned |
| 11. Framework Quality | 76–80 | Logging, secrets, linting, formatting, dependencies and flaky-test prevention | ⏳ Planned |
| 12. CI/CD with GitHub Actions | 81–85 | Automated pipelines, markers, secrets, reports and artifacts | ⏳ Planned |
| 13. Final Portfolio Project | 86–90 | Complete automation framework, documentation, CI/CD and final review | ⏳ Planned |

### Current Focus

**Chapter 4 — API Test Architecture**

Progress: Day 30 of 32

Current topics:

- Reusable API client methods
- Centralized API client class
- Request sessions and shared headers
- URL construction and normalization
- Environment configuration
- API mocking
- HTTP error handling
- Default and custom timeouts
- Query parameters and pagination
- Bearer token authentication
- JSON Schema response validation

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
