# parser.py

'''
This parser will parser any string of text of any language which has no delimiters.
These are languages such as Chinese, Hindi, Thai, etc...

'''

from itertools import zip_longest


class Trie:

    def __init__(self):
        self.root = dict()

    def add_string(self, string):
        current_node = self.root
        for pair in zip_longest(string, string[1:]):
            if (pair[0] not in current_node and
                pair[1] is not None):
                current_node[pair[0]] = { pair[1] : dict() }
            elif (pair[0] not in current_node and
                pair[1] is None):
                current_node[pair[0]] = pair[1]
            current_node = current_node[pair[0]]

    def find_match(self, string):
        current_node = self.root
        try:
            for c in string:
                current_node = current_node[c]
        except KeyError:
            return False
        return True



class Parser:


    def __init__(self, word_file):
        '''
        Words must be set before building the trie.
        '''
        self.words = word_file
        self.trie = self.build_trie()
        pass

    def parse(self, string):
        result = ''
        tokens = list()
        current = self.trie
        prev = 0
        for ix,s in enumerate(string):
            if current[s]:
                current = current[s]
            elif current[s] == None:
                tokens.append(string[prev:ix+1])
                prev = ix+1
                current = self.trie
        return tokens

    def set_wordref(self, file):
        ''' 
        Sets which file to use as the reference dictionary.
        '''
        self.words = file

    def build_trie(self):
        trie_root = dict()
        for word in self.words:
            for ix,right_char in enumerate(reversed(word)):
                if ix == 0:
                    left_char = { right_char : None }
                else:
                    current = { right_char : left_char }
                    left_char = current
            trie_root = left_char
        self.trie = trie_root
