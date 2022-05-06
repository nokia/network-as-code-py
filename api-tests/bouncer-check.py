#!/usr/bin/env python3

SERVICE_NAME = "NaC-py"
BOUNCER_INSTANCE = "http://slahtine.atg.dynamic.nsn-net.net"
DEPENDENCY_DIR = "./api-tests/api-dependencies/"

import requests
import os, sys
import json
import yaml

def get_provider_openapi():
    print("Fetching API document...")
    res = requests.get("https://gitlab.cic-nfv.com/network-as-code/nac-api/-/raw/main/api.yaml", verify = False)

    if not res.ok:
        raise ProviderUploadError(res.reason)

    openapi_object = yaml.safe_load(res.text)

    print("Fetch successful.")

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

def get_dependencies():
    collected_files = []

    for (root, dirs, files) in os.walk(DEPENDENCY_DIR):
        for file in files:
            collected_files.append(os.path.join(root, file))

    return collected_files

def upload_dependency_openapi_to_bouncer(filename):
    with open(filename) as f:
        text = f.read()

        openapi_object = yaml.safe_load(text)
        DEPENDENCY_NAME = openapi_object["info"]["title"]

        payload = {
            "service_name": SERVICE_NAME,
            "dependency_name": DEPENDENCY_NAME,
            "openapi": openapi_object
        }

        res = requests.post(f"{BOUNCER_INSTANCE}/dependency", json=payload)

        if not res.ok:
            raise DependencyCheckError(SERVICE_NAME, res.reason, res.text)


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
        sys.exit(os.EX_SOFTWARE)

    print("Finding dependencies...")
    dependencies = get_dependencies()

    print("Uploading dependencies...")
    for dep in dependencies:
        print(f"Dependency: {dep}")
        try:
            upload_dependency_openapi_to_bouncer(dep)
        except DependencyCheckError as err:
            print(f"FAILED: {dep} | {err}")
            sys.exit(os.EX_SOFTWARE)

    print("All good!")

if __name__ == "__main__":
    main()
