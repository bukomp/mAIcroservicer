#!/bin/bash

#! Save requirements to the requirements.txt
pipreqs ./pythonVersion --force

# Run tests for the CLI application

# Run tests for the web server

# Read the current version number from a file
version=$(cat version.txt)

# Increment the version number
version=$((version + 1))

# Write the new version number back to the file
echo $version > version.txt

# Build the Docker image with the new version number
docker build --build-arg VERSION=$version -t ai-service:$version ./gptVersion
