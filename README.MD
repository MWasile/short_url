# About the project
 This is a simple web application that can shorten long links into shorter ones. The application uses a unique algorithm to generate short, random identifiers for each link. In addition to shortening links, the application also provides an endpoint ("/reverse/") that allows users to retrieve the original link. The application is designed to be user-friendly and accessible to everyone who needs to shorten their links.
# Requirements
- Docker

# Technologies
- Django Rest Framework
- drf-spectacular
- pytest
- mypy
- black

# How to run
- clone the repository
- go to the project folder
- fill `.env` file with your values (you can use `backend/envs/backend_env-default.env` as an example)
- run `docker compose up --build`

# How to test
- run `docker compose exec backend_api pytest`

# How to check code style
- run `docker compose exec backend_api black .`

# How to check types
- run `docker compose exec backend_api mypy .`

# How to check code coverage
- run `docker compose exec backend_api pytest --cov=. --cov-report=html`
- open `htmlcov/index.html` in your browser
- check the coverage report

# How to check API documentation
- run project as described in `How to run` section
- open `http://localhost:8000/api/schema/swagger-ui/"` in your browser
- check the API documentation
- open `http://localhost:8000/api/schema/redoc/` in your browser
