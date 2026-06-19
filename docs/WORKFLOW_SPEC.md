# Workflow Specification

FlowFFmpeg accepts a declarative JSON document and compiles it into an inspectable FFmpeg argument list.

## Top-level fields

| Field | Type | Required | Description |
|---|---|---:|---|
| `input` | string | yes | Source media path |
| `output` | string | yes | Planned output path |
| `nodes` | array | no | Ordered processing nodes |

## Supported nodes

### Trim

```json
{"type":"trim","start":10,"duration":30}
```

`start` and `duration` are expressed in seconds.

### Scale

```json
{"type":"scale","width":-2,"height":1080}
```

A width of `-2` delegates aspect-ratio-preserving width calculation to FFmpeg.

### Frame rate

```json
{"type":"fps","value":30}
```

### Volume

```json
{"type":"volume","value":1.0}
```

### Codec

```json
{"type":"codec","video":"libx264","audio":"aac"}
```

## Compilation guarantees

- Unknown node types fail before command output.
- Arguments are constructed as a list rather than concatenated shell input.
- The CLI only prints the command in the current MVP.
- The compiler does not verify that media paths or codecs exist.

## Future schema rules

A versioned schema should reject negative duration, non-finite numeric values, unsupported codec identifiers, duplicate singleton nodes, and output paths equal to the input path unless explicitly allowed.
