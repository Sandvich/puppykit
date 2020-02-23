#!/usr/bin/env bash

# Make sure we're on master, with the latest changes, and all local changes have been discarded.
git reset --hard HEAD
git checkout master
git pull

# Sync our nginx config
cp system/puppykit.org.uk /etc/nginx/sites-available/puppykit.org.uk
test -f /etc/nginx/sites-enabled/puppykit.org.uk || ln -s /etc/nginx/sites-available/puppykit.org.uk /etc/nginx/sites-enabled/puppykit.org.uk

# Sync our systemd service
cp system/puppykit.service /etc/systemd/system/docker.puppykit.service
systemctl daemon-reload

# Stop and delete the old version of the site container
systemctl stop docker.puppykit
docker rm puppykit

# Build the new container and launch it
docker build -t puppykit .
docker run -p 80:80 --name puppykit -d -e WORKERS_PER_CORE="1" puppykit
docker stop puppykit
systemctl start docker.puppykit

