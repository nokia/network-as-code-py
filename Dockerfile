FROM fedora:43

WORKDIR /sdk

RUN dnf upgrade -y && \
    dnf install -y  podman-docker jq git nodejs && \
    echo 'unqualified-search-registries = ["docker.io"]' >> /etc/containers/registries.conf && \
    npm install -g fern-api

CMD ["fern", "-v"]
