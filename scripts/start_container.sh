#!/bin/bash

# Get the image with the highest tag
IMAGE=$(docker images --format '{{.Repository}}:{{.Tag}}' | grep 'ai-service' | sort -V | tail -n 1)


# Run the container with the highest tag
CONTAINER_ID=$(docker run -d -p 127.0.0.1:3000:3000 $IMAGE)

if [ $? -eq 0 ]; then
  echo "Container started successfully with ID: $CONTAINER_ID"
else
  echo "
  Failed to start container. Trying to stop and start again.
  "
  docker stop $(docker ps -q --filter ancestor=$IMAGE)
  docker rm $(docker ps -a -q --filter ancestor=$IMAGE)

  if docker run -d -p 127.0.0.1:3000:3000 $IMAGE; then
    echo "
    Container started successfully after retry."
  else
    echo "
    Failed to start container after retry."
  fi
fi
