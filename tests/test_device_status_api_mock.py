import httpx
from pytest_httpx import httpx_mock
from network_as_code.api.location_api import LocationAPI
from network_as_code.models.device_status import ConnectivitySubscription

import pytest