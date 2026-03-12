#! /bin/sh

set -eu

# Fetch Network as Code API spec from staging environment

curl --request POST \
	--url https://graphql-platform.p-eu.rapidapi.com/ \
	--header 'Content-Type: application/json' \
	--header 'x-rapidapi-host: graphql-platform.nokia-stage.rapidapi.com' \
	--header "x-rapidapi-identity-key: $RAPID_IDENTITY" \
	--header "x-rapidapi-key: $RAPID_KEY" \
	--data '{"query":"query MyQuery {\n  exportOpenApi(apiId: \"api_47e41e89-ab4a-40fa-87de-c528077c9945\")\n}"}' \
    | jq ".data.exportOpenApi" > openapi/rapid-spec-oas.json 


# The Fern TS generator produces faulty code due to enums in orphan schemas.
# Since the necessary schemas are all inline, the ones under components.schemas
# are all orphans and should not be reflected in the generated code.

jq 'del(.components.schemas)' openapi/rapid-spec-oas.json > openapi/rapid-spec-oas-no-schemas.json 
