# Windows Guide

FlowFFmpeg produces a preview of media-processing arguments. Review the preview before using it with a local FFmpeg installation.

## Setup checks

- Confirm FFmpeg is installed from a trusted source.
- Confirm the terminal can locate the FFmpeg executable.
- Restart the terminal after changing environment variables.
- Keep workflow files in UTF-8.

## Path checks

- Use clear project folders for input and output.
- Quote paths that contain spaces.
- Keep the output path different from the input path.
- Create the output folder before processing.
- Check available disk space.

## Compatibility checks

- FFmpeg builds may support different encoders.
- Non-ASCII filenames should be tested with the installed build.
- PowerShell and Command Prompt handle quoting differently.
- Test one file before starting a large batch.

## Troubleshooting record

When reporting a problem, include the Windows version, terminal type, FFmpeg version, workflow file, generated preview, and the visible error message. Remove private paths and personal information before sharing logs.

## Production record

For repeatable output, preserve the workflow checksum, FFmpeg version, selected preset, output checksum, and review date.
