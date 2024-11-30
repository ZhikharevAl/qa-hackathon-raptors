
---

Test Case: Verify User List API

**ID**: TC-001
**Objective**: Ensure that the API returns the correct list of users.

---

## Description

Verify that the API:

1. Returns the `meta` and `users` keys in the response.
2. The `meta.total` field correctly indicates the number of users.
3. Each user contains mandatory keys with non-empty values:
   - `avatar_url`
   - `email`
   - `name`
   - `nickname`

Additionally, verify that the offset works correctly:

1. Ensure the first user from the initial list is not present in the next page.

---

## Preconditions

1. Authorization is performed using a valid token.
2. Users exist in the system.

---

## Steps

1. Send a `GET /users` request with a valid `Task-Id`.
2. Retrieve and process the API response.
3. Validate the structure and content of the response using assertions.

---

## Expected Result

- API returns the `meta` and `users` keys.
- The `meta.total` field is greater than 0 if the user list is not empty.
- Each user has valid values for the keys:
- The first user from the initial list is not present in the next page, verifying the offset functionality.

---

## Postconditions

Log out of the session.

---
