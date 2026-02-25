# Reservation Validation API

## Build & Test
- Language: Python (stdlib + http.server) OR Node.js (stdlib + http module)
- Run: python main.py / node index.js
- Test: python -m pytest tests/ / node test.js
- Port: 3000

## Conventions
- No external dependencies -- stdlib only (no Express, no Flask, no pip/npm install)
- In-memory data storage (dictionary/object, no database)
- RESTful endpoint naming: plural nouns (/reservations, not /reservation)
- JSON request and response bodies
- Consistent error response format: {"error": {"code": "VALIDATION_ERROR", "message": "..."}}
- HTTP status codes: 200 OK, 201 Created, 400 Bad Request, 404 Not Found, 429 Too Many Requests
- Input validation on every endpoint before processing

## Business Rules
- Valid parks: Magic Kingdom, EPCOT, Hollywood Studios, Animal Kingdom
- Party size: 1-20
- Date range: today through 60 days from now
- Max 3 active reservations per guest email

## Don't
- Don't install any packages (no pip install, no npm install)
- Don't use external frameworks (no Express, Flask, FastAPI, etc.)
- Don't make network requests to external services
- Don't use a database (SQLite, PostgreSQL, etc.)
- Don't use hardcoded absolute paths
