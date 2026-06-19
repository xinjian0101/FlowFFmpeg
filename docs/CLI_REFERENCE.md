# Command-Line Reference

## Command

```bash
python main.py <workflow.json>
```

The command reads a JSON workflow and prints the generated FFmpeg command preview.

## Input requirements

A workflow requires:

- `input`: source media path
- `output`: planned output path
- `nodes`: ordered operation list

## Supported node types

### Trim

```json
{"type":"trim","start":10,"duration":30}
```

### Scale

```json
{"type":"scale","width":1920,"height":1080}
```

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

## Output behavior

The current CLI prints a shell-readable preview. Application integrations should use argument arrays and avoid converting untrusted values into free-form shell input.

## Error behavior

The compiler rejects missing input or output fields and unsupported node types. Schema validation should be performed before command generation in larger integrations.

## Reproducibility record

Store the workflow file, workflow checksum, compiler commit, generated argument list, operating system, FFmpeg version, result code, and output checksum.
