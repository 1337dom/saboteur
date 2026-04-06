# Test Design Example

Scenario: a retry helper was patched to stop after three attempts, and the first instinct is to add one happy-path test plus one exhaustion test.

## Naive First Plan

- Test that the helper retries twice and succeeds on the third attempt.
- Test that it throws after three failures.
- Stop there.

Why it sounds appealing:

- low effort
- covers the obvious branch
- easy to read

## Sabotage Phase

### Counterexamples

- Cancellation between attempts may still schedule a fourth timer.
- The helper may stop after three attempts for thrown errors but not for rejected promises.
- Jitter or backoff math may leak extra delay or skip a retry boundary.

### Alternative Root-Cause Explanation

- The defect may not be the attempt counter at all. It may be duplicate scheduling or shared mutable state between retry runs.

### Hidden Assumptions

- Assumes sync throws and async rejects behave the same.
- Assumes retries are isolated per invocation.
- Assumes cancellation clears scheduled work.

### Regression Risks

- Retry cancellation still leaks timers.
- Error classification may retry non-retryable failures.
- Shared state may contaminate concurrent callers.

### Edge Cases

- cancellation after attempt two
- concurrent callers using the same helper instance
- non-retryable status codes
- jitter value at minimum and maximum bounds
- idempotent callback invoked under partial success

### Likely Missing Tests

- cancellation prevents future scheduling
- reject path and throw path both honor the limit
- concurrent invocations do not share attempt counters
- non-retryable failures stop immediately
- jitter math stays within bounds

## Revised Safer Plan

Build a small adversarial test matrix:

- success on final allowed attempt
- exhaustion after max retries
- cancellation before the next scheduled retry
- thrown error vs rejected promise parity
- non-retryable failure short-circuit
- concurrent invocation isolation
- jitter/backoff bound assertions

Why it is safer:

- It tests the surfaces most likely to produce false confidence.
- It checks boundaries, not just the “normal” path.

## What Changed After Self-Critique

Before sabotage:

- “Prove the helper works.”

After sabotage:

- “Try to make the helper fail at its exact boundary conditions.”

## Minimal Patch Scope

- targeted retry helper tests
- no unrelated helper refactor

## Non-Goals

- No timing abstraction rewrite.
- No generalized resilience framework.
