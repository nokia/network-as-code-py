
# Changelog

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