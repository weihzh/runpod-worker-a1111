#!/usr/bin/env bash

echo "Webui Initiated"

echo "Starting WebUI API"
/runpod-volume/stable-diffusion-webui/webui.sh -f --xformers --enable-insecure-extension-access --no-half-vae --disable-model-loading-ram-optimization --port 3000 --api --listen --skip-version-check  --no-hashing --no-download-sd-model & 

# Keep the script running to prevent the container from exiting
wait