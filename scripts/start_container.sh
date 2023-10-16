#!/bin/bash

# Get the image with the highest tag
IMAGE=$(docker images --format '{{.Repository}}:{{.Tag}}' | grep 'ai-service' | sort -V | tail -n 1)

# Run the container with the highest tag
docker run -d -p 127.0.0.1:3000:3000 $IMAGE
