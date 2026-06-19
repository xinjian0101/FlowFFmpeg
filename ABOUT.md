# About FlowFFmpeg

## Mission

FlowFFmpeg turns reviewed declarative media workflows into deterministic FFmpeg argument lists without automatically executing external processes.

## Intended users

- Developers building media-processing interfaces
- Teams that need inspectable command generation
- Batch-export systems with a separate controlled runner
- Video editors preserving reproducible processing settings

## Core capabilities

- Trim, scale, frame-rate, volume, crop, and codec nodes
- Workflow validation
- Deterministic option ordering
- Shell-readable and JSON argument output
- Versioned schemas and presets
- Explicit failure for unsupported nodes

## Boundaries

The project does not execute FFmpeg, probe source media, manage queues, retry failed jobs, or guarantee encoder availability.

## Architecture

```text
JSON workflow -> validation -> ordered node compilation
              -> filter construction -> argument array -> preview
```

## Design priorities

1. Declarative workflows
2. No arbitrary shell fragments
3. Deterministic arguments
4. Strict validation
5. Separation of compilation and execution
6. Reproducible processing records

## Maturity

The project is an executable MVP with schemas, presets, validation, crop support, tests, platform guidance, and batch-manifest planning.

## Security model

A separate runner must control paths, protocols, overwrite behavior, timeouts, resources, logging, and FFmpeg versions.

## Governance

Every new node requires validation rules, command fixtures, compatibility notes, and tests. Public documentation and examples are maintained in English.
