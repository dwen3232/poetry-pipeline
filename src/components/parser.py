from typing import Union, List
from src.parsers import PARSER_MAP


def parser_comp(
        text_file_name,
        *,
        parser_type: str = 'poetry',
        parse_by_stanza: bool = False,
        implicit_lines_per_stanza: int = 4
) -> Union[List[List[str]], List[str]]:
    parser = PARSER_MAP[parser_type]().load_file(text_file_name)
    output = parser.parse(
        parse_by_stanza=parse_by_stanza,
        implicit_lines_per_stanza=implicit_lines_per_stanza
    )
    return output
