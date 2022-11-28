import os
import requests
from typing import List
import replicate
NEGATIVE_PROMPT = "text, alphabet, words, caption, nsfw"


class StableDiffusionWithNegativePrompt:
    def __init__(self):
        # https://replicate.com/stability-ai/stable-diffusion
        self.model = replicate.models.get("cjwbw/stable-diffusion").versions.get("4049a9d8947a75a0b245e3937f194d27e3277bab4a9c1d6f81922919b65175fd")

    def predict(self, prompts: List[str], output_dir_name: str,
                *,
                use_previous_image_as_init: bool = False,
                width: int = 512,
                height: int = 512,
                prompt_strength: float = 0.8,
                num_inference_steps: int = 50,
                guidance_scale: float = 7.5
                ):
        if not prompts:
            raise ValueError('prompts should be non-empty')

        # create the dir if it doesn't exist
        output_dir = f'./outputs/{output_dir_name}'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        else:
            raise ValueError('output_dir_name already exists')

        img_urls = []
        file_paths = []
        prompts_file = open(f'{output_dir}/prompts.txt', 'w')

        for i, prompt in enumerate(prompts):
            init_image = img_urls[i-1] if use_previous_image_as_init and i != 0 else None
            output = self.model.predict(prompt=prompt,
                                        negative_prompt=NEGATIVE_PROMPT,
                                        init_image=init_image,
                                        width=width,
                                        height=height,
                                        prompt_strength=prompt_strength,
                                        num_inference_steps=num_inference_steps,
                                        guidance_scale=guidance_scale
                                        )
            img_urls.append(output[0])
            # write image to local
            img_data = requests.get(output[0]).content
            file_name = f'{output_dir}/{i}.png'
            with open(file_name, 'wb') as f:
                f.write(img_data)
            file_paths.append(file_name)
            prompts_file.write(f'{prompt}\n\n')

        prompts_file.close()
        return img_urls, file_paths
