#!/bin/bash

# Check if Docker is running
if ! docker info >/dev/null 2>&1; then
    echo "Docker is not running. Terminating script execution."
    return
fi

if [ -z "$n" ]
then
    microservice=$(ls -v ./microservices | tail -n 1)
    microservice_version=$(echo $microservice | cut -d '-' -f 2)
    microservice_name=$(echo $microservice | cut -d '-' -f 4 | cut -d '/' -f 1)
else
    microservice_version=$(echo $n | cut -d '-' -f 2)
    microservice_name=$(echo $n | cut -d '-' -f 4 | cut -d '/' -f 1)
fi

echo $microservice_name

version=$(docker images | grep $microservice_name | sort -r | head -n 1 | awk '{print $2}')
if [ -z "$version" ]
then
    version="1.0.0"
else
    version=$(echo $version | awk -F. -v OFS=. '{$NF++;print}')
fi



# Build the Docker image with the new version number
docker build --build-arg VERSION=$version -t $microservice_name:$version ./microservices/-$microservice_version--$microservice_name || { echo 'Docker build failed' ; return; }
