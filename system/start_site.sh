#!/usr/bin/env bash

sudo podman build -t puppykit ..
sudo podman run \
        -p 8080:80 \
        --name puppykit \
        -d \
        -e WEB_CONCURRENCY="2" \
        puppykit
