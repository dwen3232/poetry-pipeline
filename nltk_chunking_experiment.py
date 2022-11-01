from src.parsers.poetry_parser import PoetryParser
import nltk

if __name__ == '__main__':
    parser = PoetryParser()
    parser.load_file('because_i_could_not_stop_for_death.txt')
    lines = parser.parse()

    # tokenize
    tokens = nltk.word_tokenize(lines[0])
    print(tokens)

    # part of speech tagging
    tagged = nltk.pos_tag(tokens)
    print(tagged)

    # chunking
    entities = nltk.chunk.ne_chunk(tagged)
    print(entities)
    entities.draw()
