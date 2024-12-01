
---

Test Case: Verify Single User Retrieval API

**ID**: TC-002
**Objective**: Ensure that the API returns the correct user details by UUID

---

## Description

Verify that the API:

1. Returns user details for a specific UUID
2. Returns a user object with all expected keys
3. Returns the exact user matching the requested UUID

---

## Preconditions

1. Authorization is performed using a valid token
2. User with the specified UUID exists in the system

---

## Steps

1. Send a `GET /users/{user_uuid}` request with a valid `Task-Id`
2. Retrieve and process the API response
3. Validate the structure and content of the response using assertions

---

## Test Data

- Task-Id: api-23
- User UUID: 23403afa-483c-4803-8af1-2d1316f1460f

---

## Expected Result

- API returns a user object with keys:
  - avatar_url
  - email
  - name
  - nickname
  - uuid
- Returned user UUID matches the requested UUID
- User object passes Pydantic model validation

---

## Postconditions

Log out of the session

---
