
---

Test Case: Verify User Deletion API

**ID**: TC-003
**Objective**: Ensure that the API can successfully delete a user by UUID and return correct response

---

## Description

Verify that the API:

1. Accepts a valid delete request for a specific user
2. Deletes the user with the matching UUID
3. Returns appropriate response data after deletion

---

## Preconditions

1. Authorization is performed using a valid token
2. A new user exists in the system for deletion
3. User API client is configured and available

---

## Steps

1. Create a new user in the system
2. Send a `DELETE /users/{user_uuid}` request with:
   - Valid `Task-Id`
   - Correct user UUID
3. Retrieve and process the API response
4. Validate the response structure and content

---

## Test Data

- Task-Id: api-1
- User UUID: To be dynamically generated during test setup

---

## Expected Result

- API returns a successful response (status code 204)
- Returned response contains:
  - Deleted user's UUID
  - Matching UUID with the originally created user
- Response passes Pydantic model validation
- User is no longer retrievable after deletion

---

## Postconditions

1. Verify the user cannot be retrieved after deletion
2. Log out of the session

---
