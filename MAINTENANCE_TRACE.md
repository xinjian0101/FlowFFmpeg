# Maintenance Trace

Batch: `content-enrichment-2026-06-19`

## Iteration 10

- Expanded the README with use cases, workflow examples, execution guidance, security boundaries, design principles, and limitations.
- Preserved the existing compiler-only behavior and did not claim automatic FFmpeg execution.

## Iteration 11

- Added this visible maintenance trace.
- Established compatibility, validation, and security expectations for future nodes.

## Iteration 12

- Planned document: `docs/SECURITY_MODEL.md`.
- Defines trust boundaries between workflow input, compiler output, execution layer, and generated media.

## Validation record

| Check | Result |
|---|---|
| Existing CLI retained | pass |
| Compiler-only positioning retained | pass |
| Unknown-node failure behavior retained | pass |
| Shell-string execution not introduced | pass |
| Documentation links reviewed | pass after iteration 12 |

## Maintenance policy

1. New nodes require schema validation and tests.
2. Parameter order must remain deterministic.
3. Execution must stay outside the compiler unless explicitly redesigned.
4. Path, protocol, filter, and overwrite controls belong to a reviewed security policy.
5. Behavior changes require before-and-after generated-command fixtures.
6. FFmpeg-version assumptions must be documented.

## Open items

- No process runner, queue, timeout manager, or retry controller.
- No automatic media probing.
- No compatibility matrix for hardware encoders.
- No arbitrary custom-filter support in the safe baseline.
