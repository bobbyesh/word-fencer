# parser.py

'''
This parser will parser any string of text of any language which has no delimiters.
These are languages such as Chinese, Hindi, Thai, etc...
'''

class Parser:


    def __init__(self, word_file):
        '''
        Words must be set before building the trie.
        '''
        self.words = word_file
        self.dictionary = self.build_trie()
        pass

    def parse(self, string):
        result = ''
        tokens = list()
        current = self.dictionary
        prev = 0
        for ix,s in enumerate(string):
            if current[s]:
                current = current[s]
            elif current[s] == None:
                tokens.append(string[prev:ix+1])
                prev = ix+1
                current = self.dictionary
        return tokens

    def set_wordref(self, file):
        ''' 
        Sets which file to use as the reference dictionary.
        '''
        self.words = file

    def build_trie(self):
        test_dict = "ABC"
        k = dict()
        for ix,char in enumerate(reversed(test_dict)):
            if ix == 0:
                prev = { char : None }
            else:
                current = { char : prev }
                prev = current
        dictionary = prev
        dictionary["D"] = None
        dictionary["E"] = None
        return dictionary
