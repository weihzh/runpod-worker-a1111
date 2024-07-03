import requests
import base64
from io import BytesIO

input_data = {"url":"https://miro.medium.com/v2/resize:fit:450/1*WQ3dZlUXpPOAOUGmPc974Q.jpeg",
              "category":"tts",
              "batch_size":1}
location = ["beach", "bedroom", "garden", "street"]
mock_data = {
    "tts":{
            "sd_model_checkpoint": "training-model-fp16fix-VAE-baked",
            "sd_vae": "sdxl_vae_fp16_fix.safetensors",
            "prompt": ", realistic <lora:ip-adapter-faceid-plusv2_sdxl_lora:1>",
            "negative_prompt": "hands, nipples, 3d, cartoon",
            "steps": 30,
            "cfg_scale": 2,
            "width": 960,
            "height": 1280,
            "sampler_name": "DPM++ SDE",
            "sampler_index": "DPM++ SDE",
            "scheduler": "karras",
            "restore_faces": False,
            "cn_enabled": True,
            "cn_module": "ip-adapter-auto",
            "cn_model": "ip-adapter-faceid-plusv2_sdxl",
            "cn_weight": 1,
            "cn_resize_mode": "Crop and Resize",
            "cn_guidance_start": 0,
            "cn_guidance_end": 1,
            "cn_pixel_perfect": True,
            "cn_weight_type": "ease in-out"
         },
    "banner": {
            "sd_model_checkpoint": "training-model-fp16fix-VAE-baked",
            "sd_vae": "sdxl_vae_fp16_fix.safetensors",
            "prompt": "realistic photo of a woman wearing clothes <lora:ip-adapter-faceid-plusv2_sdxl_lora:1>",
            "negative_prompt": "nipples, hands, nose piercing",
            "steps": 30,
            "cfg_scale": 2,
            "width": 960,
            "height": 1280,
            "sampler_name": "DPM++ SDE",
            "sampler_index": "DPM++ SDE",
            "scheduler": "karras",
            "restore_faces": False,
            "cn_enabled": True,
            "cn_module": "ip-adapter-auto",
            "cn_model": "ip-adapter-faceid-plusv2_sdxl",
            "cn_weight": 1,
            "cn_resize_mode": "Crop and Resize",
            "cn_guidance_start": 0,
            "cn_guidance_end": 1,
            "cn_pixel_perfect": True,
            "cn_weight_type": "ease in-out"
         }
}

def image_to_base64(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Raise an exception if the request failed
    response.raise_for_status()
    # Convert the response content to a BytesIO object (to handle it as a file)
    image_bytes = BytesIO(response.content)
    # Encode the image to base64
    base64_encoded = base64.b64encode(image_bytes.getvalue())
    # Convert bytes to string
    base64_string = base64_encoded.decode('utf-8')
    return base64_string



def process_data(input_json):
    category = input_json.get('category')
    sd_params = mock_data.get(category, [])
    return {
        "api": {
            "method": "POST",
            "endpoint": "/sdapi/v1/txt2img"
        },
        "payload": {            
            "override_settings": {
            "sd_model_checkpoint": sd_params.get("sd_model_checkpoint"),
            "sd_vae": sd_params.get("sd_vae"),
            },
            "override_settings_restore_afterwards": True,
            "prompt": sd_params.get("prompt"),
            "negative_prompt": sd_params.get("negative_prompt"),
            "seed": -1,
            "batch_size": input_json.get('batch_size'),
            "steps": sd_params.get("steps"),
            "cfg_scale": sd_params.get("cfg_scale"),
            "width": sd_params.get("width"),
            "height": sd_params.get("height"),
            "sampler_name": sd_params.get("sampler_name"),
            "sampler_index": sd_params.get("sampler_index"),
            "scheduler": sd_params.get("scheduler"),
            "restore_faces": False,
            "alwayson_scripts": {
                "controlnet": {
                    "args": [
                        {
                            "module": sd_params.get("cn_module"),
                            "model": sd_params.get("cn_model"),
                            "enabled": sd_params.get("cn_enabled"),
                            "input_image": image_to_base64(input_json.get('url')),
                            "weight": sd_params.get("cn_weight"),
                            "resize_mode": sd_params.get("cn_resize_mode"),
                            "lowvram": False,
                            "guidance_start": sd_params.get("cn_guidance_start"),
                            "guidance_end": sd_params.get("cn_guidance_end"),
                            "control_mode": "Balanced",
                            "pixel_perfect": sd_params.get("cn_pixel_perfect"),
                            "weight_type": sd_params.get("cn_weight_type"),
                        }
                    ]
                }
            }
        }  
    }

test_output_1 = process_data(input_data)
print(test_output_1)


