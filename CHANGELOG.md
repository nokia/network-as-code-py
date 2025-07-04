# Changelog

## Version 6.0.0

Breaking Changes:
- Introduced one main API with all features available as separate endpoints.

Deprications:
- Slice modification endpoint is no longer supported.

## Version 5.2.1

Fixes:
- Sim Swap docstring incorrectly stated that the `max_age` was in seconds, when it is in fact in hours

Tooling:
- Project has been switched over to use the `uv` tool for managing dependencies and venvs

## Version 5.2.0

Changes:
- Introduced support for Geofencing API
- Introduced support for Number Verification API

Fixes:
- API request timeouts have been extended to 30 seconds for long-running requests
- Bumped dependency versions

## Version 5.1.1

Fixes:
- Adapted the Location Verification bindings to use the new version prefix
- Using just a public IPv4 address for a device didn't actually work and has now been fixed

## Version 5.1.0

Changes:
- Made using devices with public IPv4 address a bit easier by allowing private address to be omitted
- Upped the minimum Python version requirement to 3.11, so that some zulu-time workarounds could be removed

Fixes:
- Sources now get regularly type-checked with mypy and type issues have been resolved
- Some dependency versions have been bumped in lock file to avoid vulnerabilities

## Version 5.0.0

Breaking changes:
- Location verification using `device.verify_location()` returns a result object containing
  `match_rate`, `last_location_time` and the `result_type` fields

## Version 4.1.0

Changes:
- Location information from `device.location()` now supplies radius information
- QoD sessions can be extended with `session.extend_session()` method
- The date given by SIM Swap is now provided as `datetime`
- Docstrings have been updated across the board

## Version 4.0.1

Fixes:
- Webhook information was passed to the QoD API using an older way, but has now
  been updated to match the current behavior of the API, this has no impact on
  application code

## Version 4.0.0

Breaking changes:
- `device.create_qod_session()` now requires `duration` as a mandatory parameter
- `device.get_congestion()` now returns a list of `Congestion` objects

Changes:
- `device.verify_location()` may now return a "PARTIAL" result if the device is
  partially inside the verification area

Fixes:
- Previously due to a miscommunication `device.sessions()` would return all
  created sessions. These have now been correctly limited to device-specific ones

## Version 3.1.0

Changes:

- Introduced SIM Swap functionality to query the date of a SIM Swap event for a particular device
- Minor code cleanup and more thorough release testing

## Version 3.0.1

Fixes

-   Fixed a bug that caused `Not Found` error in fetching slice attachments
-   Prohibit the use of a device public IPv4 address as a literal string.

## Version 3.0.0

Breaking changes:

-   `slice.wait_done()` was renamed to `slice.wait_for()`
-   `client.slices.create()` parameter names now all use snake_case
-   `client.slices.getAll()` was renamed to `client.slices.get_all()`
-   `slice.attach()` parameter names now all use snake

Changes:

-   Handle ISO date strings in the QoD API instead of using Unix timestamps
-   Internal code refactors to fix linter issues
-   Improvements to test suite coverage
-   Updated dependencies

## Version 2.2.2

Breaking changes:

-   None!

Fixes

-   Fixed a bug that caused invalid QoD requests to be made when some fields were unset

## Version 2.2.1

Breaking changes:

-   None!

Changes:

-   Migrated from Pydantic 1.x to 2.x
-   Updated dependencies
-   Minor refactors and bug fixes

## Version 2.2

Breaking changes:

-   None!

Changes:

-   Updated API bindings for Device Status and integrated new connectivity and roaming status polling
-   Integrated new Congestion Insights API for querying and predicting network congestion

## Version 2.1

Breaking changes:

-   None!

Changes:

-   Introduced Slice Application Attachment for performing granular, URSP-based application slicing
    -   Uses the same `slice.attach()` method, but with optional `traffic_categories` parameter, performs full slice attachment without it
-   Created a async function `wait_done()` for awaiting slice order completion for slice management
-   Introduced slice modification functionality for changing the parameters of created slices

Fixes:

-   Miscellaneous fixes to unit and integration tests

## Version 2.0

Breaking changes:

-   QoD session `started_at` and `expires_at` timestamps are now represented as `datetime` objects
-   QoD session `.duration()` method now returns a `deltatime`

Changes:

-   Location verify and retrieval now provide a default value of 60 for `max_age`, making the parameter optional

Fixes:

-   Fixed QoD sessions not being possible to create with IPv6 addresses
-   Improved handling of missing CSI ID values in returned network slice objects
-   Various type fixes behind the scenes
