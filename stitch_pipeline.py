import dotenv
from src.components import parser_comp
from src.components import prompt_creator_comp
from src.components import diffusion_comp
from src.components import stitch_comp


def pipeline(
        text_file_name,
        output_dir_name,
        *,
        parser_type: str = 'poetry',
        parse_by_stanza: bool = False,
        implicit_lines_per_stanza: int = 4,
        prompt_creation_type: str = 'naive',
        prompt_by_stanza: bool = False,
        lines_per_prompt: int = 2,
        model_type: str = 'stable_diffusion',
        use_previous_image_as_init: bool = False,
        width: int = 512,
        height: int = 512,
        prompt_strength: float = 0.8,
        num_inference_steps: int = 50,
        guidance_scale: float = 7.5,
        font: str = 'Ubuntu-L.ttf'
):
    parser_out = parser_comp(text_file_name, parser_type=parser_type,
                             parse_by_stanza=parse_by_stanza,
                             implicit_lines_per_stanza=implicit_lines_per_stanza)

    print('parser_out: ', parser_out)
    prompt_creator_out = prompt_creator_comp(parser_out, prompt_creation_type=prompt_creation_type,
                                             prompt_by_stanza=prompt_by_stanza,
                                             lines_per_prompt=lines_per_prompt)
    print('prompt_creator_out', prompt_creator_out)
    img_urls, file_paths = diffusion_comp(prompt_creator_out, output_dir_name,
                                       model_type=model_type,
                                       use_previous_image_as_init=use_previous_image_as_init,
                                       width=width,
                                       height=height,
                                       prompt_strength=prompt_strength,
                                       num_inference_steps=num_inference_steps,
                                       guidance_scale=guidance_scale)
    print('diffusion_out', file_paths)
    stitch_comp(file_paths, parser_out, font=font)


if __name__ == '__main__':
    dotenv.load_dotenv()

    kwargs = {
        'text_file_name': 'aedh_wishes_for_the_cloths_of_heaven.txt',
        # 'text_file_name': 'poverty.txt',
        'output_dir_name': 'parrot_test_aedh_1',

        'parser_type': 'poetry',
        'parse_by_stanza': True,
        'implicit_lines_per_stanza': 4,

        'prompt_creation_type': 'parrot',
        'prompt_by_stanza': True,
        'lines_per_prompt': 4,

        'model_type': 'stable_diffusion_negative',
        'use_previous_image_as_init': True,
        'width': 512,
        'height': 512,
        'prompt_strength': 0.8,
        'num_inference_steps': 50,

        'font': 'Tomatoes-O8L8.ttf'
    }

    pipeline(**kwargs)
