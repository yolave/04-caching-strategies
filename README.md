# Caching strategies: Techniques to reduce latency and improve performance through effective caching

A simple **FastAPI** application demonstrating caching strategies, clean architecture, and integration with third-party APIs.


## Features

- RESTful endpoints with FastAPI
- Clean Architecture (Separation of Concerns)
- Pydantic models for validation and type safety
- In-memory DB through repository pattern
- JWT token validation (assumed from external OAuth2 provider)
- Communication with third-party APIs (hexagonal architecture)
- Auto-generated API docs via Swagger (OpenAPI)
- Unit tests
- Caching using Redis and FastAPI's built-in cache

## Run Redis (using Docker compose) 
```bash
docker compose up -d
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the app

```bash
uvicorn src.main:app --reload
```

### Authorization (JWT)
Use header `Authorization: Bearer valid-token`

---

### 📁 Project Structure

```
04-caching-strategies/
├── src/
│   ├── __init__.py
│   ├── main.py                      # FastAPI app initialization and routing
│   ├── api/                         
│   │   ├── routes.py                # Entry point for all API routes
│   │   └── endpoints/               
│   │       └── users.py             # User-related route handlers
│   ├── models/                      
│   │   └── user.py                  # Pydantic models for input/output validation
│   ├── services/                    
│   │   └── user_service.py          # Business logic layer (application use cases)
│   ├── ports/                       
│   │   └── db_port.py               # Interfaces/abstract classes (Hexagonal Architecture)
│   ├── adapters/                    
│   │   └── memory_db.py             # In-memory implementation of the data access layer
│   ├── external/                    
│   │   └── third_party.py           # Wrapper to interact with 3rd-party APIs
│   └── core/                        
│       ├── config.py                # Application settings using Pydantic
│       └── security.py              # JWT validation logic
├── tests/                           
│   ├── api/                         # Tests for API endpoints
│   │   ├── endpoints/               
│   │   │   └── test_users.py        # Unit tests for user endpoints
│   ├── services/                    # Tests for service layer
│   │   └── test_user_service.py     # Unit tests for user service logic
├── requirements.txt                 # Python dependencies
├── requirements_test.txt            # Python dependencies for testing
├── conftest.py                      # Pytest configuration
├── docker-compose.yml               # Docker Compose file to run Redis
├── README.md                        # Project documentation
```

---

### 🧱 Explanation of Responsibilities

| Folder / File           | Purpose & Responsibility                                                                |
|-------------------------|-----------------------------------------------------------------------------------------|
| `src/main.py`           | Creates the FastAPI app, includes routers, and serves as the entry point                |
| `src/api/routes.py`     | Organizes all route groups (e.g., `/users`, `/products`, etc.)                          |
| `src/api/endpoints/`    | Contains route handlers, handling request/response and delegating to services           |
| `src/models/`           | Defines data contracts using Pydantic for input validation and output schemas           |
| `src/services/`         | Contains application-level use cases (business logic), keeping route handlers thin      |
| `src/ports/`            | Declares interfaces (aka "ports") for dependencies like data sources (DB, cache, etc.)  |
| `src/adapters/`         | Implements concrete adapters like an in-memory DB or external provider                  |
| `src/external/`         | Communication logic with third-party services (e.g., LLMs, external APIs)               |
| `src/core/config.py`    | Global configuration, ideally using Pydantic’s `BaseSettings`                           |
| `src/core/security.py`  | Encapsulates authentication logic (e.g., checking a JWT token from a header)            |
| `tests/`                | Contains unit tests and integration tests using FastAPI's `TestClient`                  |
| `requirements.txt`      | Pinning core dependencies to install the project                                        |
| `requirements_test.txt` | Pinning testing dependencies (e.g., pytest, httpx) for running tests                    |
| `conftest.py`           | Pytest configuration for fixtures and shared test setup                                 |
| `README.md`             | Explanation of the project, its structure, and usage                                    |
| `docker-compose.yml`    | Configuration to run Redis in a Docker container for caching                            |
