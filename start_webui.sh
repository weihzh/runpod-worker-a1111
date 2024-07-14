#!/usr/bin/env bash

echo "Webui Initiated"

ln -s /runpod-volume /workspace

# Check and activate the virtual environment
if [ -f "/workspace/venv/bin/activate" ]; then
    echo "Activating virtual environment"
    source /workspace/venv/bin/activate
    TCMALLOC="$(ldconfig -p | grep -Po "libtcmalloc.so.\d" | head -n 1)"
    export LD_PRELOAD="${TCMALLOC}"
    export PYTHONUNBUFFERED=true
    export HF_HOME="/workspace"
    
    echo "Starting WebUI API"
    /runpod-volume/stable-diffusion-webui/webui.sh -f --xformers --enable-insecure-extension-access --no-half-vae --disable-model-loading-ram-optimization --port 3000 --api --listen --skip-version-check --no-hashing --no-download-sd-model &

    # Deactivate the virtual environment
    deactivate
else
    echo "ERROR: The Python Virtual Environment (/workspace/venv/bin/activate) could not be activated"
    echo "1. Ensure that you have followed the instructions at: https://github.com/ashleykleynhans/runpod-worker-a1111/blob/main/docs/installing.md"
    echo "2. Ensure that you have used the Pytorch image for the installation and NOT a Stable Diffusion image."
    echo "3. Ensure that you have attached your Network Volume to your endpoint."
    echo "4. Ensure that you didn't assign any other invalid regions to your endpoint."
fi

# Keep the script running to prevent the container from exiting
wait
