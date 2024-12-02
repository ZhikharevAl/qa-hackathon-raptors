[![Ruff Linter](https://github.com/ZhikharevAl/qa-hackathon-raptors/actions/workflows/ruff_check.yml/badge.svg)](https://github.com/ZhikharevAl/qa-hackathon-raptors/actions/workflows/ruff_check.yml)

# API Defect Hunt 🕵️‍♀️🔍

## Project Overview

This is a comprehensive API testing framework designed to systematically identify and report defects in web service interfaces using Python, Playwright, and advanced testing methodologies.

## Tech Stack 🛠️

- **Language**: Python 3.10+
- **Virtual Environment**: `uv`
- **Testing Framework**:
  - Pytest
  - Playwright
- **Validation**:
  - Pydantic
- **Linting**: Ruff
- **Pre-commit Hooks**: `pre-commit`
- **Reporting**: Allure
- **Parallel Execution**: pytest-xdist

## Prerequisites 📋

- Python 3.10+
- `uv`
- `pip`

## Setup & Installation 🚀

### 1. Clone the Repository

```bash
git clone https://github.com/ZhikharevAl/qa-hackathon-raptors.git
cd qa-hackathon-raptors
```

### 2. Create Virtual Environment with uv

```bash
uv venv  # Creates a new virtual environment
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
uv pip install -r requirements.txt
uv pip install pre-commit
pre-commit install
```

### 4. Configure Environment Variables

Create a `.env` file with necessary credentials:

```
API_TOKEN=your_api_token_here
```

## Development Tools 🛠️

### Linting with Ruff

```bash
ruff check .  # Check for linting issues
ruff format .  # Format code
```

### Pre-commit Hooks

Automatically run before each commit:

- Linting
- Formatting
- Type checking
- Other configured checks

## Pydantic Validation 🔍

### Key Features

- Strict type validation
- Data parsing
- Schema generation
- Runtime type checking

### Example Model


```python
from pydantic import BaseModel, Field

class UserResponse(BaseModel):
    uuid: str = Field(..., description="UUID of the user")
    email: str = Field(..., description="Email address of the user")
    name: str = Field(..., description="Name of the user")
    nickname: str = Field(..., description="Nickname of the user")
```

## Running Tests 🧪

### All Tests

```bash
pytest
```

### Parallel Execution

```bash
pytest -n auto  # Automatically detect available CPU cores
```

### Specific Test Suite

```bash
pytest tests/test_users.py
```

## Generating Allure Reports 📊

### 1. Run Tests with Allure Tracking

```bash
pytest --alluredir=allure-results
```

### 2. Generate HTML Report

```bash
allure serve allure-results
```

## Project Structure

```
project-root/
│
├── tests/               # Test suites
│   ├── test_users.py
│   └── ...
│
├── services/            # API service classes
│   ├── users/
│   │   └── models/     # Pydantic models
│   └── ...
│
├── config/              # Configuration files
├── utils/               # Utility modules
├── requirements.txt     # Dependency list
└── .pre-commit-config.yaml  # Pre-commit configuration
```

## Best Practices 📘

- Use `uv` for dependency management
- Utilize Ruff for consistent code quality
- Leverage pre-commit hooks
- Use Pydantic for robust data validation
- Create comprehensive Pydantic models
- Use fixtures for test setup/teardown
- Parameterize tests
- Validate response schemas

## License

[MIT](LICENSE.md)
