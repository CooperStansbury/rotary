"""
A class to facilitate English language generation based on
inputs
"""


import spacy

# compact lib to start
nlp = spacy.load('en_core_web_sm')


class Roter():
    """A class to manage cut-up generation
    """


    def get_lines(self, input_filepath):
        """A method to read a text file line by
        line and return a list

        Args:
            input_filepath (string): filepath
        Returns:
            lines (list of string): breaks file down by line
        """
        return [line.strip() for line in open(input_filepath, 'r')\
            if not len(line) == 1]


    def SPACY_THAT(self, lines):
        """A method to parse the input using spacy

        Args:
             lines (list of string): file by line
         Returns:
            doc_obj (spacy.Tokens.doc)
        """
        input_string = "\n".join(lines)
        return nlp(input_string)
        print(input_string)


    def __init__(self, input_filepath):
        # for both, keys are lower-case strings for single words
        # data steructure for part of speech
        # and markov chain
        self.POS = {}
        self.CHAIN = {}

        self.lines = self.get_lines(input_filepath)
        # set spacy attr
        self.doc_obj = self.SPACY_THAT(self.lines)

        # build the chain
        for idx, token in enumerate(self.doc_obj):
            # no partials
            if idx == 0:
                continue

            if not token in self.CHAIN:
                self.CHAIN[token] = [self.doc_obj[idx-1]]
            else:
                self.CHAIN[token].append(self.doc_obj[idx-1])

        [print(k, v) for k, v in self.CHAIN.items()]
