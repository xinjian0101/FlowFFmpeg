# Support

## Start here

Review these documents before opening an issue:

- [README](README.md) for supported nodes and examples
- [About](ABOUT.md) for compiler boundaries and maturity
- [Workflow Specification](docs/WORKFLOW_SPEC.md) for node contracts
- [Security Model](docs/SECURITY_MODEL.md) for execution boundaries
- [Safety Checklist](docs/SAFETY_CHECKLIST.md) for command review
- [Windows Guide](docs/WINDOWS_GUIDE.md) for platform-specific handling

## Bug reports

Use the structured **Bug report** form for workflow validation, option ordering, filter generation, codec arguments, overwrite behavior, shell display, or JSON-array output.

Include:

- exact commit or release;
- operating system and Python version;
- FFmpeg version when execution behavior is relevant;
- minimal JSON workflow;
- generated argument array;
- expected argument array or validation result;
- private paths replaced with synthetic paths.

## Feature requests

Use the **Feature request** form. Define the media workflow, proposed declarative syntax, validation rules, expected argument ordering, compatibility impact, and security boundaries.

## Security boundaries

Do not report issues by pasting credentials, internal paths, private URLs, or untrusted shell fragments. FlowFFmpeg compiles arguments only; process execution, sandboxing, timeouts, resources, protocols, and artifact validation belong to a separate runner.

## Project boundaries

FlowFFmpeg does not provide:

- automatic FFmpeg execution;
- queue or retry management;
- automatic media probing;
- unrestricted custom filter strings;
- guarantees that every encoder exists in every FFmpeg build.

## Response expectations

Support is best effort. Minimal workflows with exact generated arguments are more useful than screenshots or broad descriptions without reproducible input.
