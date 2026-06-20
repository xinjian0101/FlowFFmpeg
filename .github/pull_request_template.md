## Summary

Describe the workflow node, validation, argument output, preset, test, or documentation change.

## Behavior

- Previous command behavior:
- New command behavior:
- Compatibility impact:

## Verification

- [ ] Added validation tests
- [ ] Added generated-argument tests
- [ ] Ran `python -m unittest -v`
- [ ] Checked shell-readable output
- [ ] Checked JSON argument output
- [ ] Confirmed input and output paths remain distinct
- [ ] Confirmed node order is deterministic

## Security boundaries

- [ ] No free-form shell fragment was introduced
- [ ] New string fields are validated
- [ ] Overwrite behavior is explicit
- [ ] Execution remains outside the compiler
- [ ] Network and device inputs remain unsupported unless separately reviewed

## Documentation

- [ ] Updated README or workflow specification
- [ ] Added or updated a preset when useful
- [ ] Recorded user-visible behavior changes

## Reviewer notes

List FFmpeg-version assumptions, platform differences, limitations, and follow-up work.
