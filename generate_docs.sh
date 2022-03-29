#!/usr/bin/env bash

mkdir -p docs/

poetry run pydoc-markdown -m network_as_code.Configuration --render-toc > docs/Configuration.md
poetry run pydoc-markdown -m network_as_code.CustomNetworkProfile --render-toc > docs/CustomNetworkProfile.md
poetry run pydoc-markdown -m network_as_code.DeviceLocation --render-toc > docs/DeviceLocation.md
poetry run pydoc-markdown -m network_as_code.Device --render-toc > docs/Device.md
poetry run pydoc-markdown -m network_as_code.GeoZone --render-toc > docs/GeoZone.md
poetry run pydoc-markdown -m network_as_code.NetworkProfile --render-toc > docs/NetworkProfile.md
