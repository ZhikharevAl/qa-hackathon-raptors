# Bug Report: Unexpected Game Search Behavior

**ID**: BUG-GAMES-001
**Title**: Game Search Returns Unrelated Games Instead of Exact Title Match for [test case](/docs/TestCases/Test_case_game_search_005.md)

## Description

When searching for a game by its exact title ("Elden Ring"), the API returns a list of 10 unrelated games that do not match the search query.

## Steps to Reproduce

1. Call the `search_games` method
2. Use Task-Id: `api-2`
3. Pass query: `"Elden Ring"`

## Expected Result

- A list of games containing ONLY games with the title "Elden Ring"
- Number of results: 1 or more, but all with the same title

## Actual Result

Returned a list of 10 different games:
1. Elden Ring
2. Baldur's Gate 3
3. The Sims 4
4. The Elder Scrolls V: Skyrim
5. The Witcher 3: Wild Hunt
6. Red Dead Redemption 2
7. Forza Horizon 5
8. Atomic Heart
9. The Last of Us
10. Uncharted 4: A Thief's End

## Technical Details

- Method: `search_games()`
- Endpoint: `/games/search/`
- Task-Id: `api-2`

## Impact

**High** - Breaks game search logic, makes exact title search impossible

## Recommended Actions

1. Review backend game search method implementation
2. Ensure search query works correctly
3. Fix result filtering logic
4. Add server-side validation for `query` parameter

## Priority

**High** - Critical for game search functionality

## Potential Root Causes

- Incorrect search algorithm
- Lack of precise filtering
- Incorrect query handling in backend

## Reproducibility

- Consistently reproducible
- Occurs with Task-Id api-2
- Requires immediate investigation
