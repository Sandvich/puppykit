#!/usr/bin/env bash

# Sync our nginx config
cp puppykit.org.uk /etc/nginx/sites-available/puppykit.org.uk
test -f /etc/nginx/sites-enabled/puppykit.org.uk || ln -s /etc/nginx/sites-available/puppykit.org.uk /etc/nginx/sites-enabled/puppykit.org.uk

# Make sure we're on master, with the latest changes, and all local changes have been discarded.
git reset --hard HEAD
git checkout master
git pull

# Stop and delete the old version of the site container
docker stop puppykit
docker rm puppykit

# Build the new container and launch it
docker build -t puppykit .
docker run -p 8080:80 --name puppykit -d puppykit
