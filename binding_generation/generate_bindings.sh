#! /bin/sh

java -jar openapi-generator-cli.jar generate -i qos-api.json -o qos_client -g python --additional-properties packageName=qos_client
