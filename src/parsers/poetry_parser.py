from typing import Union, List

POETRY_DIR = './inputs/poetry'


class PoetryParser:
    """
    Parser class for poetry texts
    """
    def __init__(self):
        self.input_file_name = None
        self.input_file_path = None
        self.input_file_contents = None

    def load_file(self, file: str):
        """
        Loads poetry text file

        :param file: file name of poem to parse
        :return: self
        """
        self.input_file_name = file
        self.input_file_path = f"{POETRY_DIR}/{file}"
        with open(self.input_file_path) as f:
            self.input_file_contents = f.read()

        return self

    def get_file_contents(self):
        """
        Returns the contents of the input file
        """
        return self.input_file_contents

    def parse(self,
              *,
              parse_by_stanza: bool = False,
              implicit_lines_per_stanza: int = 4
              ) -> Union[List[List[str]], List[str]]:
        """
        Parses the poem at either line-level or stanza-level using the following steps
            1.  Split the input text by line using newline chars. If there are empty lines separating stanzas, then
                they will appear as empty strs
            2.  If `parse_by_stanza` flag is enabled, split the lines by stanza. If there are empty lines, they are used as
                the delimiters, otherwise, `implicit_lines_per_stanza` is used.
            3. Return either stanzas or lines. Remove any empty lines.

        :param parse_by_stanza: bool indicating whether to split at the stanza level
        :param implicit_lines_per_stanza: int for number of lines per stanza, only used if no empty lines are found
        :return: the parsed text
        """
        # 1. Split text by line
        lines = self.input_file_contents.split('\n')

        # 2. Split lines by stanza
        stanzas = []
        if parse_by_stanza:
            # if we have an empty string, we can break by stanza using empty str lines
            if '' in lines:
                # get line indices with empty strings
                break_idx = [-1] + [idx for idx, line in enumerate(lines) if line == '']
                stanzas = [lines[break_idx[i] + 1: break_idx[i+1]] for i in range(len(break_idx) - 1)]
                stanzas.append(lines[break_idx[-1] + 1:])

            # otherwise, we need to implicitly break by stanza
            else:
                # break stanzas into blocks of `implicit_lines_per_stanza`
                n = implicit_lines_per_stanza
                stanzas = [lines[i * n: (i+1) * n] for i in range((len(lines) + n - 1) // n)]

        # 3. Return either the stanzas or lines
        return stanzas if parse_by_stanza else [line for line in lines if line != '']
