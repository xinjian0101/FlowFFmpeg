# Maintenance Trace

This file records visible maintenance work applied to FlowFFmpeg.

## Maintenance cycle 1

- Expanded the repository entry point.
- Added execution guidance, security boundaries, design principles, and limitations.
- Preserved the compiler-only baseline.

## Maintenance cycle 2

- Added workflow specifications, presets, schemas, safety checklists, and platform guidance.

## Maintenance cycle 3

- Added batch-manifest support documentation and additional review presets.

## Maintenance cycle 4 — English-only repository content

### Iteration 71

- Replaced the Chinese README with a full English guide.
- Corrected the documented workflow example to use the implemented `nodes` structure and node field names.

### Iteration 72

- Added an English command-line reference for all supported node types.

### Iteration 73

- Updated this trace and confirmed the English-only documentation policy.

## Verification

| Check | Result |
|---|---|
| Existing CLI retained | pass |
| Compiler-only positioning retained | pass |
| Unsupported-node failure retained | pass |
| README example matches implementation | pass |
| English README completed | pass |
| English CLI reference completed | pass |

## Maintenance rules

1. New nodes require schema validation and tests.
2. Argument order must remain deterministic.
3. Execution remains outside the compiler unless explicitly redesigned.
4. Path, protocol, filter, and overwrite controls require review.
5. Behavior changes require generated-command fixtures.
6. FFmpeg version assumptions must be documented.
7. User-facing repository content is maintained in English.

## Open work

- Process runner and queue management
- Automatic media probing
- Hardware encoder compatibility matrix
- Controlled advanced-filter support
