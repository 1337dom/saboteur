# Bug Fix Example

Scenario: search results sometimes show stale data when a user types quickly in a search box.

## Naive First Plan

- Increase the debounce from 150ms to 400ms.
- Assume fewer requests will eliminate the bug.
- Touch only the input handler.

Why it sounds appealing:

- small change
- easy to explain
- probably reduces network traffic

## Sabotage Phase

### Counterexamples

- Older request still resolves after the newer request and overwrites the latest results.
- Slower debounce makes the bug less frequent without actually removing the race.
- Users on fast networks may still see stale flashes because response ordering, not request frequency, is the real problem.

### Alternative Root-Cause Explanation

- The bug may come from response reordering or stale state writes, not from “too many requests.”

### Hidden Assumptions

- Assumes request count is the cause.
- Assumes the UI writes only the latest response.
- Assumes slower typing latency is acceptable UX.

### Regression Risks

- Search feels sluggish.
- Keyboard-driven workflows become worse.
- Existing tests may still pass while the race survives.

### Edge Cases

- Rapid delete and retype.
- Empty query followed by a non-empty query.
- Late response after navigation away or cancellation.

### Likely Missing Tests

- Verify older requests cannot overwrite newer state.
- Verify cancellation or invalidation on rapid successive queries.
- Verify loading state does not flicker incorrectly on aborted requests.

## Revised Safer Plan

- Track a request identity for each search.
- Ignore or cancel stale responses when a newer request exists.
- Keep the debounce unchanged unless UX data says otherwise.
- Add a regression test for out-of-order resolution.

Why it is safer:

- It addresses the race directly.
- It does not trade correctness for slower UX.
- It keeps the patch inside the request lifecycle instead of changing broader input behavior.

## What Changed After Self-Critique

Before sabotage:

- “Reduce requests.”

After sabotage:

- “Make stale requests unable to win.”

## Minimal Patch Scope

- Search request lifecycle
- state update guard for stale responses
- one or two focused regression tests

## Non-Goals

- No search service rewrite.
- No new caching layer.
- No input-component redesign.
