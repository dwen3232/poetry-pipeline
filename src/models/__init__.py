from .stable_diffusion import StableDiffusion
from .stable_diffusion_with_negative_prompt import StableDiffusionWithNegativePrompt

MODEL_MAPPING = {
    'stable_diffusion': StableDiffusion,
    'stable_diffusion_negative': StableDiffusionWithNegativePrompt
}