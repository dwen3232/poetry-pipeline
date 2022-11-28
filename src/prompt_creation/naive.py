from typing import Union, List
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
from rake_nltk import Rake
import nltk
import re
nltk.download('stopwords')
nltk.download('punkt')

class NaivePromptCreator:
    def generate_prompt(self,
                        parsed_text: Union[List[List[str]], List[str]],
                        *,
                        prompt_by_stanza: bool = False,
                        lines_per_prompt: int = 2
                        ) -> List[str]:
        """
        Creates prompts naively (doesn't do any sort of processing at all. Mostly for POC)

        :param parsed_text: the parsed text
        :param prompt_by_stanza: creates prompt at stanza level if True
        :param lines_per_prompt: number of lines to use per prompt
        :return: generated prompts
        """
        if not isinstance(parsed_text[0], list) and prompt_by_stanza:
            raise ValueError('expected parsed_text to be List[List[str]] if prompt_by_stanza')

        prompts = []
        n = lines_per_prompt
        # case where we generate multiple prompts per stanza
        if isinstance(parsed_text[0], list) and not prompt_by_stanza:
            for stanza in parsed_text:
                stanza_prompts = ['\n'.join(self.collect_noun_phrases(stanza[i * n: (i + 1) * n])) for i in range((len(stanza) + n - 1) // n)]
                prompts += stanza_prompts
        # case where we generate single prompt per stanza
        elif isinstance(parsed_text[0], list) and prompt_by_stanza:
            prompts = ['\n'.join(self.collect_noun_phrases(stanza)) for stanza in parsed_text]
        # case where we generate prompts by line
        elif not isinstance(parsed_text[0], list):
            prompts = ['\n'.join(self.collect_noun_phrases(parsed_text[i * n: (i + 1) * n])) for i in range((len(parsed_text) + n - 1) // n)]

        return prompts
    
    def collect_noun_phrases(self, prompt):
        r = Rake()
        res = []
        r.extract_keywords_from_sentences(prompt)
        pat = "|".join(r.get_ranked_phrases())
        for line in prompt:
            if (len(line) == 0):
                continue
            line = str.lower(line)
            res.append(" ".join(re.findall(pat, line)))
        
        return res
        
