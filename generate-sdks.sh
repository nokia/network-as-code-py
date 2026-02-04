#! /bin/sh

set -eux

fern check

fern generate --local --no-prompt
