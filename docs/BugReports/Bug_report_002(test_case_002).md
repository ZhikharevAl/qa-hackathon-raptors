
---

# Bug Report [for the test case 002](/docs/TestCases/Test_CaseVerify_Single_UserRetrieval_002.md)

**ID**: BUG-002
**Title**: API Returns Incorrect User for Requested UUID

---

## Description

When requesting a specific user by UUID, the API returns a different user's details than the one requested.

---

## Steps to Reproduce

1. Send a `GET /users` request with the following parameters:
   - Task-Id: api-23
   - User UUID: 23403afa-483c-4803-8af1-2d1316f1460f

2. Verify the returned user's UUID

---

## Expected Result

The API should return a user with the UUID 23403afa-483c-4803-8af1-2d1316f1460f

---

## Actual Result

The API returns a user with a different UUID:

- Requested UUID: 23403afa-483c-4803-8af1-2d1316f1460f
- Returned UUID: 2ed46da7-2d96-4da2-af16-74dfc34174ca

---

## Impact

High - This indicates a critical issue with the user retrieval endpoint, where the API is not correctly filtering users by their UUID.

---

## Recommended Actions

1. Investigate the user retrieval logic in the backend
2. Verify the database query or filtering mechanism
3. Ensure that the API correctly matches and returns the user with the exact requested UUID

---

## Additional Notes

- The test case uses Pydantic validation to ensure the response structure
- All expected keys are present in the returned user object
- The discrepancy is solely in the UUID matching

---
