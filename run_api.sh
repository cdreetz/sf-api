#!/bin/bash

# Define the Docker image name
IMAGE_NAME=my_fastapi_app

# Build the Docker image
docker build -t $IMAGE_NAME .

# Run the Docker container
docker run -d --name my_fastapi_container -p 1313:1313 $IMAGE_NAME
