# Test Case: Validate Exact Game Title Search

**ID**: TC-GAMES-001
**Objective**: Verify Precise Game Search Functionality

## Description

Ensure game search works correctly and returns ONLY games with an exact title match

## Preconditions

1. Games API is available
2. Authorization is performed
3. Test environment is prepared

## Test Steps

1. Prepare a search query with an exact game title
2. Call `search_games` method
3. Validate response
4. Check search result consistency

## Test Data

- Task-Id: `api-2`
- Query: `"Elden Ring"`
- Expected Fields:
  - `title`: Exact match
  - `price`: Non-negative number
  - `uuid`: Non-empty value

## Expected Result

- Returns a list of games
- ALL games have IDENTICAL title "Elden Ring"
- Each game passes model validation

## Postconditions

- Clear search results
- Verify no side effects

## Notes

- Search is case-insensitive
- Strict result validation required

## Risks

- Incorrect search may lead to poor user navigation

## Acceptance Criteria

- Exact title match
- Correct game data
- Result consistency

## Test Environment

- API Endpoint: `/games/search/`
- Test Framework: pytest
- Validation: Pydantic models

## Additional Considerations

- Performance testing
- Edge case handling
