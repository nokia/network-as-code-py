#! /bin/sh

set -eux

fern check

rm -r network-as-code-py/network_as_code/
rm -r network-as-code-ts/network_as_code/

fern generate --local --no-prompt
