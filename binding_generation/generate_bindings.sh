#! /bin/sh

rm -rf qos_client/*
java -jar openapi-generator-cli.jar generate -i qos-api.json -o qos_client -g python --additional-properties packageName=qos_client

rm -rf location_client/*
java -jar openapi-generator-cli.jar generate -i location-api.json -o location_client -g python --additional-properties packageName=location_client

rm -rf devicestatus_client/*
java -jar openapi-generator-cli.jar generate -i devicestatus-api.json -o devicestatus_client -g python --additional-properties packageName=devicestatus_client --skip-validate-spec
