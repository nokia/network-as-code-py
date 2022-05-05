#!/usr/bin/env python3

SERVICE_NAME = "NaC-py"
BOUNCER_INSTANCE = "http://slahtine.atg.dynamic.nsn-net.net:8000"

import requests
import os, sys
import json
import yaml

def get_provider_openapi():
    res = requests.get("https://gitlab.cic-nfv.com/network-as-code/nac-api/-/raw/main/api.yaml", verify = False)

    openapi_object = yaml.safe_load(res.text)

    return openapi_object

def upload_provider_openapi_to_bouncer(openapi_object):
    SERVICE_NAME = openapi_object["info"]["title"]

    payload = {
        "service_name": SERVICE_NAME,
        "openapi": openapi_object
    }

    res = requests.post(f"{BOUNCER_INSTANCE}/provider", json=payload)

    if not res.ok:
        raise ProviderUploadError(SERVICE_NAME, res.reason, res.text)

class ProviderUploadError(Exception):
    """Represent a failed dependency check"""

class DependencyCheckError(Exception):
    """Represent a failed dependency check"""

def main():
    print("Uploading endpoint information...")
    try:
        upload_provider_openapi_to_bouncer(get_provider_openapi())
    except ProviderUploadError as err:
        print(f"FAILED: {err}")

    print("All good!")

if __name__ == "__main__":
    main()
