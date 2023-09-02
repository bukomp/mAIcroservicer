#!/bin/bash

# Get the image with the highest tag
IMAGE=$(docker images --format '{{.Repository}}:{{.Tag}}' | grep 'random-number-generator-service' | sort -V | tail -n 1)

# Run the container with the highest tag
docker run -d -p 3000:3000 $IMAGE
