# Refactor Example

Scenario: duplicated authorization checks exist in three endpoints, and a naive cleanup plan wants to centralize everything into one helper.

## Naive First Plan

- Move all authorization logic into `auth/permissions.ts`.
- Replace local checks in all endpoints with one shared helper.
- Clean up related logging while touching the code anyway.

Why it sounds appealing:

- less duplication
- more “consistent” authorization logic
- refactor and cleanup in one pass

## Sabotage Phase

### Counterexamples

- One endpoint performs audit logging immediately before rejecting; moving the logic may drop that side effect.
- One caller checks permissions before loading a resource, another after loading and ownership comparison; a single helper may flatten meaningful differences.
- One path returns `404` to avoid resource existence leaks, while the others return `403`; a shared helper may accidentally change that behavior.

### Alternative Root-Cause Explanation

- The real problem may not be “duplicated logic.” The real problem may be that one endpoint is missing a single predicate while the rest are intentionally different.

### Hidden Assumptions

- Assumes the checks are semantically identical.
- Assumes side effects around the checks are accidental.
- Assumes centralization is safer than local clarity.

### Regression Risks

- Authorization semantics drift.
- Audit logging disappears or moves.
- Error-shape behavior changes and breaks clients or security expectations.

### Edge Cases

- Soft-deleted resources.
- Admin override paths.
- Ownership checks that require loaded state.

### Likely Missing Tests

- Endpoint-specific error behavior.
- Audit logging on denied access.
- Admin and owner matrix coverage per endpoint.

## Revised Safer Plan

- Extract only the pure shared predicate that is actually duplicated.
- Keep endpoint-local ordering, logging, and response shaping where they already live.
- Fix the missing predicate in the one problematic endpoint.
- Add focused tests around denied-access behavior and audit logging.

Why it is safer:

- It removes duplication without flattening behavior that is intentionally local.
- It narrows the patch to the actual risky logic instead of redesigning the whole authorization flow.

## What Changed After Self-Critique

Before sabotage:

- “Unify all authorization logic.”

After sabotage:

- “Extract the pure shared predicate, keep local side effects local.”

## Minimal Patch Scope

- one shared predicate
- one endpoint fix
- behavior-preserving tests

## Non-Goals

- No auth subsystem rewrite.
- No new policy DSL.
- No cross-endpoint response normalization.
