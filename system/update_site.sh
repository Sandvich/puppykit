#!/usr/bin/env bash

# Make sure we're on master, with the latest changes, and all local changes have been discarded.
git reset --hard HEAD
git checkout master
git pull

# Stop and delete the old version of the site container
sudo podman stop puppykit
sudo podman rm puppykit

# Build and launch the new version
./start_site.sh
