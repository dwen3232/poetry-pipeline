from typing import Union, List
from src.prompt_creation import PROMPT_CREATION_MAP


def prompt_creator_comp(
        parsed_text: Union[List[List[str]], List[str]],
        *,
        prompt_creation_type: str = 'naive',
        prompt_by_stanza: bool = False,
        lines_per_prompt: int = 2
):
    prompt_creator = PROMPT_CREATION_MAP[prompt_creation_type]()
    prompts = prompt_creator.generate_prompt(parsed_text,
                                             prompt_by_stanza=prompt_by_stanza,
                                             lines_per_prompt=lines_per_prompt)
    return prompts
