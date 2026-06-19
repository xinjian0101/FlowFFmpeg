# FlowFFmpeg

FlowFFmpeg compiles declarative JSON media workflows into inspectable FFmpeg argument lists. It converts trim, scale, frame-rate, volume, and codec nodes into a deterministic command preview while keeping execution outside the compiler.

> Status: safe command-generation layer, not a full editor and not an automatic process runner.

## Use cases

- Convert application settings into FFmpeg arguments
- Review input, output, filter, timing, and codec choices before execution
- Preserve reproducible media-processing configurations
- Prepare batch-job manifests for a separate execution service
- Pass approved highlight intervals into a controlled media pipeline

## Current capabilities

- Trim nodes
- Scale nodes
- Frame-rate nodes
- Volume nodes
- Codec nodes
- Immediate failure for unsupported node types
- Argument-list construction instead of free-form shell strings
- Command preview without automatic execution

## Requirements

- Python 3.10 or newer
- FFmpeg is not required when only generating a preview
- A local FFmpeg installation is required when a separate runner executes the result

## Run

```bash
python main.py examples/workflow.json
```

## Test

```bash
python tests.py
```

## Workflow example

```json
{
  "input": "input.mp4",
  "output": "output.mp4",
  "nodes": [
    {"type": "trim", "start": 12.0, "duration": 30.0},
    {"type": "scale", "width": 1080, "height": 1920},
    {"type": "fps", "value": 30},
    {"type": "volume", "value": 1.0},
    {"type": "codec", "video": "libx264", "audio": "aac"}
  ]
}
```

Use the committed examples and schema as the source of truth. New nodes should include explicit validation, examples, compatibility notes, and tests.

## Recommended execution flow

1. Create a JSON workflow in the application layer.
2. Compile it with FlowFFmpeg.
3. Review paths, overwrite behavior, timing, filters, and codecs.
4. Execute the argument list in a separate controlled runner.
5. Record the FFmpeg version, workflow checksum, generated arguments, and result code.
6. Verify the output file with a media probe.

## Safety boundaries

- The project does not execute commands by default.
- Do not concatenate untrusted values into a shell string.
- Restrict output paths in the execution layer.
- Configure timeouts, resource limits, bounded retries, and logs outside the compiler.
- Require explicit approval before overwriting files.
- Apply additional allowlists before supporting network inputs, device inputs, or advanced custom filters.

## Design principles

- **Declarative**: workflows describe approved operations rather than arbitrary commands.
- **Inspectable**: generated arguments can be reviewed and rejected.
- **Deterministic**: the same version and input should produce the same argument order.
- **Strict**: unsupported nodes fail instead of being ignored.
- **Separated responsibilities**: compilation, execution, monitoring, and artifact validation remain independent.

## Presets

- `presets/vertical-short.json`
- `presets/social-landscape.json`
- `presets/audio-copy-review.json`

Presets are starting points. Review dimensions, duration, codecs, and paths for each source.

## Known limitations

- The node set covers only a small part of FFmpeg.
- The compiler does not probe source media automatically.
- It does not manage processes, retries, queues, or parallel execution.
- It does not yet support complex filter graphs or hardware-encoder compatibility checks.
- Generated arguments may require platform-specific review.

## Documentation

- [Workflow Specification](docs/WORKFLOW_SPEC.md)
- [Command Review Checklist](docs/SAFETY_CHECKLIST.md)
- [Windows Guide](docs/WINDOWS_GUIDE.md)
- [Security Model](docs/SECURITY_MODEL.md)
- [Maintenance Trace](MAINTENANCE_TRACE.md)

## License

MIT
