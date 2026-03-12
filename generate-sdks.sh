#! /bin/sh

set -eux

fern check

rm -r network-as-code-py/network_as_code/ || true
rm -r network-as-code-ts/network_as_code/ || true

fern generate --local --no-prompt
