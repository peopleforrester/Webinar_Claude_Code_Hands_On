---
name: api-scaffold
description: Scaffolds REST API endpoints with input validation, error handling, and tests. Use when creating API endpoints or microservices.
---
When creating an API endpoint:

## Validation Pattern
- Validate all inputs at the top of every handler before any processing
- Return early on validation failure with a 400 status
- Use a shared validation helper for common patterns (email, date range, enum membership)

## Error Response Format
Always return errors in this shape:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human-readable description of what went wrong"
  }
}
```
Standard error codes: VALIDATION_ERROR, NOT_FOUND, RATE_LIMITED, INTERNAL_ERROR

## HTTP Status Codes
- 200 OK — successful GET, successful DELETE
- 201 Created — successful POST that creates a resource
- 400 Bad Request — validation failure
- 404 Not Found — resource does not exist
- 429 Too Many Requests — rate limit exceeded
- 500 Internal Server Error — unexpected failure

## Test Structure
- One test file per endpoint group
- Test happy path first, then each validation rule, then edge cases
- Test format: given (setup), when (call), then (assert status + body)
- Include a test for every error code the endpoint can return

## Middleware Order
1. Request logging (method, path, timestamp)
2. Rate limiting
3. Input parsing (JSON body)
4. Route handler
5. Error handler (catch-all)
