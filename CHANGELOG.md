# Changelog

## Unreleased

### Added

- Declarative workflow specification.
- Vertical short-form command-generation preset.
- Trim, scale, frame-rate, volume, and codec nodes.
- Deterministic command preview.
- Unit smoke test and GitHub Actions workflow.
- Roadmap for schema validation and batch planning.

### Security behavior

- The MVP prints an argument-safe command representation and does not execute it.
- Unknown nodes fail before command generation.
- Users must review paths, codecs, and filters before using the generated command elsewhere.

### Known limitations

- No crop, pad, subtitle, or hardware-encoder nodes.
- No media probing or codec availability checks.
- No path existence validation.
- No platform-specific escaping guarantee outside the displayed command representation.

## 0.1.0 — 2026-06-19

Initial JSON-to-FFmpeg command compiler MVP.

## Maintenance policy

- Workflow fields require versioned documentation.
- New nodes require positive and negative fixtures.
- Command generation must remain separate from execution.
- Platform-specific behavior must be documented and tested explicitly.
