from typing import Union, List
from src.models import MODEL_MAPPING


def diffusion_comp(
        prompts: List[str], output_dir_name: str,
        *,
        model_type: str = 'stable_diffusion',
        use_previous_image_as_init: bool = False,
        width: int = 512,
        height: int = 512,
        prompt_strength: float = 0.8,
        num_inference_steps: int = 50,
        guidance_scale: float = 7.5
):
    model = MODEL_MAPPING[model_type]()
    output = model.predict(prompts, output_dir_name,
                           use_previous_image_as_init=use_previous_image_as_init,
                           width=width,
                           height=height,
                           prompt_strength=prompt_strength,
                           num_inference_steps=num_inference_steps,
                           guidance_scale=guidance_scale)
    return output
