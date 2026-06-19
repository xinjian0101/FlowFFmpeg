# Command Review Checklist

FlowFFmpeg currently generates commands but does not execute them. Review every generated command before use.

## Input and output

- Confirm the input file exists and is the intended source.
- Confirm the output path is different from the input path.
- Confirm the output directory exists and has sufficient free space.
- Confirm overwrite behavior is acceptable.

## Timing

- Confirm trim start is not negative.
- Confirm duration is greater than zero.
- Confirm trim boundaries are inside the source duration.
- Confirm time units are seconds.

## Video processing

- Confirm target dimensions preserve or intentionally change aspect ratio.
- Confirm the frame-rate conversion is necessary.
- Confirm scaling does not create unwanted distortion.
- Confirm the selected video codec is installed.

## Audio processing

- Confirm volume values are intentional.
- Confirm the selected audio codec is installed.
- Confirm silent or missing audio streams are handled by the downstream command.

## Platform review

- Review quoting behavior on the target shell.
- Avoid copying untrusted paths directly into another shell command.
- Prefer argument arrays when integrating the compiler into an application.
- Record the workflow file and generated command with production logs.

## Batch processing

For batch jobs, isolate failures by input file, avoid overwriting successful outputs, keep retry counts bounded, and preserve a machine-readable task log.

## Approval record

For production workflows, record the workflow checksum, compiler commit, generated command, reviewer, execution environment, result code, and output checksum.
