from .naive import NaivePromptCreator
from .parrot import ParrotPromptCreator

PROMPT_CREATION_MAP = {
    'naive': NaivePromptCreator,
    'parrot': ParrotPromptCreator
}