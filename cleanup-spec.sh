#! /bin/sh

set -eux

# The Fern TS generator produces faulty code due to enums in orphan schemas.
# Since the necessary schemas are all inline, the ones under components.schemas
# are all orphans and should not be reflected in the generated code.

jq 'del(.components.schemas)' openapi/rapid-spec-oas.json > openapi/rapid-spec-oas-no-schemas.json 
