#!/bin/bash

echo "Start build"
docker buildx build --platform linux/amd64 -f Dockerfile_tokyo -t weihzh/runpod-worker-a1111:prod . --no-cache

echo "Pushing"
docker push weihzh/runpod-worker-a1111:prod
