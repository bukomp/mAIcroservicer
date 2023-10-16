#!/bin/bash

# Check if Docker is running
if ! docker info >/dev/null 2>&1; then
    echo "Docker is not running. Terminating script execution."
    return
fi

# Run tests for the CLI application

# Run tests for the web server

# Read the current version number from a file
# Check if a version number is provided as an argument
if [ -z "$1" ]
then
    # Check if version.txt exists, if not create it with 0 as content
    if [ ! -f version.txt ]; then
        echo 0 > version.txt
    fi
    
    # If no version number is provided, read the current version number from a file
    version=$(cat version.txt)
    echo "./microservices/microservice$version"
    echo $version

    # Check if the microservice file exists
    if [ ! -f "./microservices/microservice$version" ]; then
        echo "Microservice file v$version does not exist. Terminating script execution."
        return
    fi

    # Write the new version number back to the file
    echo $((version + 1)) > version.txt
else
    # If a version number is provided, use it
    version=$1
fi

# Build the Docker image with the new version number
docker build --build-arg VERSION=$version -t ai-service:$version ./microservices/microservice$version || { echo 'Docker build failed' ; return; }
