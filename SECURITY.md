# Security Policy

## Supported versions

Security fixes target the current `main` branch. Historical commits and unsupported forks may not receive updates.

## Reporting a vulnerability

Do not place credentials, private URLs, internal file paths, untrusted media identifiers, or working exploit details in a public issue.

Use GitHub private vulnerability reporting when available. If it is unavailable, open a minimal public issue identifying the affected commit and component without sensitive details.

Include:

- affected commit;
- minimal synthetic workflow;
- generated argument array;
- impact summary;
- operating system and Python version;
- FFmpeg version when relevant.

## Security boundaries

FlowFFmpeg compiles argument arrays but does not execute FFmpeg. The execution layer must control file paths, protocols, overwrite behavior, environment variables, timeouts, process resources, logs, and artifact validation.

Free-form shell fragments, network inputs, and device inputs are outside the current supported contract.

## Out of scope

- vulnerabilities in FFmpeg itself;
- unsafe behavior introduced by a separate runner;
- unsupported custom filters;
- leaked credentials already embedded in user workflows;
- unsupported local modifications.

## Disclosure

Allow maintainers reasonable time to reproduce, correct, test, and document a confirmed issue before public disclosure.
