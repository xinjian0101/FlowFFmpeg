<div align="center">

# FlowFFmpeg

**Declarative, inspectable FFmpeg command generation without automatic execution.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-2ea44f)](LICENSE)
[![Mode](https://img.shields.io/badge/Mode-Compiler%20Only-6f42c1)](ABOUT.md)
[![Status](https://img.shields.io/badge/Status-Active%20MVP-f59e0b)](MAINTENANCE_TRACE.md)

[Quick start](#quick-start) · [Nodes](#supported-nodes) · [Presets](#presets) · [Security](docs/SECURITY_MODEL.md) · [About](ABOUT.md)

</div>

---

FlowFFmpeg converts reviewed JSON workflows into deterministic FFmpeg argument arrays. It validates node parameters, preserves operation order, and keeps process execution outside the compiler so applications can inspect or reject commands before running them.

> [!IMPORTANT]
> FlowFFmpeg does not execute FFmpeg. A separate runner must enforce path controls, protocol restrictions, timeouts, resource limits, logging, and overwrite policy.

## At a glance

| Area | Current support |
|---|---|
| Input | Declarative JSON workflow |
| Nodes | Trim, crop, scale, pad, FPS, volume, codec |
| Validation | Numeric, path, node, color, and overwrite checks |
| Output | Shell-readable command or JSON argument array |
| Presets | Vertical, landscape, and audio-review examples |
| Runtime | Python standard library |

## Quick start

```bash
python main.py examples/workflow.json
```

Generate a JSON argument array for another process runner:

```bash
python main.py examples/workflow.json --format json
```

Run tests:

```bash
python -m unittest -v
```

## Capability matrix

| Capability | Status | Notes |
|---|---:|---|
| Deterministic argument order | ✅ | Stable compilation order |
| Input/output path separation | ✅ | Same path is rejected |
| Explicit overwrite policy | ✅ | Generates `-y` or `-n` |
| Video filter composition | ✅ | Preserves node order |
| JSON argument output | ✅ | Suitable for `subprocess` integration |
| Media probing | ⏳ | Planned separate component |
| Automatic command execution | ❌ | Intentionally outside scope |

## Supported nodes

| Node | Main fields | Generated behavior |
|---|---|---|
| `trim` | `start`, `duration` | Input seek and duration options |
| `crop` | `width`, `height`, `x`, `y` | Video crop filter |
| `scale` | `width`, `height` | Video scale filter |
| `pad` | `width`, `height`, `x`, `y`, `color` | Canvas padding filter |
| `fps` | `value` | Frame-rate filter |
| `volume` | `value` | Audio volume filter |
| `codec` | `video`, `audio` | Output codec options |

## Workflow example

```json
{
  "input": "input.mp4",
  "output": "output.mp4",
  "overwrite": false,
  "nodes": [
    {"type": "trim", "start": 12, "duration": 30},
    {"type": "crop", "width": 1080, "height": 1080, "x": 100, "y": 0},
    {"type": "scale", "width": 720, "height": 720},
    {"type": "pad", "width": 1080, "height": 1920, "x": 180, "y": 600, "color": "black"},
    {"type": "fps", "value": 30},
    {"type": "volume", "value": 1.0},
    {"type": "codec", "video": "libx264", "audio": "aac"}
  ]
}
```

## Recommended integration

```text
application settings
      ↓
JSON workflow
      ↓
FlowFFmpeg validation
      ↓
argument-array compilation
      ↓
human or policy review
      ↓
separate controlled runner
      ↓
media probe and artifact verification
```

## Presets

| Preset | Purpose |
|---|---|
| `presets/vertical-short.json` | Vertical short-form output |
| `presets/social-landscape.json` | Landscape social output |
| `presets/audio-copy-review.json` | Conservative audio review |

Presets are starting points. Review paths, dimensions, codecs, duration, and encoder availability before execution.

## Repository map

| Path | Purpose |
|---|---|
| `main.py` | Workflow validation and compilation |
| `schema/` | Workflow and batch-manifest contracts |
| `presets/` | Reviewable workflow examples |
| `examples/` | Minimal runnable workflow |
| `docs/` | Specification, safety, Windows, and security guidance |
| `test_*.py` | Validation, ordering, crop, pad, and overwrite tests |
| `ABOUT.md` | Mission, maturity, boundaries, and governance |

## Safety boundaries

- No free-form shell fragments
- No automatic process execution
- No network or device input support
- No hidden overwrite behavior
- No assumption that every FFmpeg build supports every encoder

## Documentation

- [About the project](ABOUT.md)
- [Workflow specification](docs/WORKFLOW_SPEC.md)
- [Command review checklist](docs/SAFETY_CHECKLIST.md)
- [Windows guide](docs/WINDOWS_GUIDE.md)
- [Security model](docs/SECURITY_MODEL.md)
- [CLI reference](docs/CLI_REFERENCE.md)
- [Maintenance trace](MAINTENANCE_TRACE.md)
- [Changelog](CHANGELOG.md)

## License

MIT
