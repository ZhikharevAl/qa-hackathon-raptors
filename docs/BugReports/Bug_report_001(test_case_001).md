
---

# Bug Report [for the test case 001](/docs/TestCases/Test_case_001_Verify%20User%20List.md)

**ID**: BUG-001
**Title**: API Fails to Validate User List and Offset Functionality

---

## Description

The test cases for the Users API are failing under certain conditions. Specifically, the `meta.total` value is not greater than 0 when users are present, and the first user from the initial list appears in the second list when using an offset.

---

## Steps to Reproduce

1. Send a `GET /users` request with `Task-Id` set to `api-21`.
2. Verify the `meta.total` field in the response.
3. Send a `GET /users` request with `Task-Id` set to `api-6` and an offset of 10.
4. Verify that the first user from the initial list is not present in the second list.

---

## Expected Result

1. The `meta.total` field should be greater than 0 if there are users present.
2. The first user from the initial list should not be present in the second list when using an offset of 10.

---

## Actual Result

1. `meta.total` is not greater than 0 even when users are present (Task-Id: api-21).
2. The first user from the initial list is present in the second list with an offset of 10 (Task-Id: api-6).

---

## Logs/Error Messages

- `FAILED tests/test_users.py::TestUsersAPI::test_get_users[api-21] - AssertionError: Meta 'total' should be greater than 0 for Task-Id api-21`
- `FAILED tests/test_users.py::TestUsersAPI::test_get_users[api-6] - AssertionError: First user UUID 2ed46da7-2d96-4da2-af16-74dfc34174ca from initial list should not be present in the second list with offset=10`

---

## Additional Information

- Ensure that the `meta.total` field correctly reflects the number of users.
- Verify that pagination and offset functionality work as expected and that the first user from the initial list does not appear in the subsequent pages when using an offset.

---
