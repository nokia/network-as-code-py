
# Changelog

## Version 3.0.0

Breaking changes:
- `slice.wait_done()` was renamed to `slice.wait_for()`
- `client.slices.create()` parameter names now all use snake_case
- `slice.attach()` parameter names now all use snake

Changes:
- Handle ISO date strings in the QoD API instead of using Unix timestamps
- Internal code refactors to fix linter issues
- Improvements to test suite coverage
- Updated dependencies

## Version 2.2.2

Breaking changes:
- None!

Fixes
- Fixed a bug that caused invalid QoD requests to be made when some fields were unset

## Version 2.2.1

Breaking changes:
- None!

Changes:
- Migrated from Pydantic 1.x to 2.x
- Updated dependencies
- Minor refactors and bug fixes

## Version 2.2

Breaking changes:
- None!

Changes:
- Updated API bindings for Device Status and integrated new connectivity and roaming status polling
- Integrated new Congestion Insights API for querying and predicting network congestion

## Version 2.1

Breaking changes:
- None!

Changes:
- Introduced Slice Application Attachment for performing granular, URSP-based application slicing
  - Uses the same `slice.attach()` method, but with optional `traffic_categories` parameter, performs full slice attachment without it
- Created a async function `wait_done()` for awaiting slice order completion for slice management
- Introduced slice modification functionality for changing the parameters of created slices

Fixes:
- Miscellaneous fixes to unit and integration tests

## Version 2.0

Breaking changes:
- QoD session `started_at` and `expires_at` timestamps are now represented as `datetime` objects
- QoD session `.duration()` method now returns a `deltatime`

Changes:
- Location verify and retrieval now provide a default value of 60 for `max_age`, making the parameter optional

Fixes:
- Fixed QoD sessions not being possible to create with IPv6 addresses
- Improved handling of missing CSI ID values in returned network slice objects
- Various type fixes behind the scenes
