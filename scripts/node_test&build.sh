#!/bin/bash

# Run tests for the CLI application
npm --prefix ./tsVersion/cli-app test &&

# Run tests for the web server
npm --prefix ./tsVersion/web-server test &&

# Read the current version number from a file
version=$(cat version.txt)

# Increment the version number
version=$((version + 1))

# Write the new version number back to the file
echo $version > version.txt

# Build the Docker image with the new version number
docker build --build-arg VERSION=$version -t random-number-generator-service:$version ./tsVersion
