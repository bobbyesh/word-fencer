# parser.py

'''
This parser will parser any string of text of any language which has no delimiters.
These are languages such as Chinese, Hindi, Thai, etc...

'''

from trie import Trie

class ParserError(Exception):

    def __init__(self, message):
        self.message = message




class Parser(object):


    def __init__(self, word_file):
        '''
        Initializes parser with a word reference file.

        '''
        self.trie = Trie()
        self.word_file = word_file
        self.populated = False
    
    def parse(self, string):
        '''
        Returns a list of all the longest valid tokens in string.
        This follows a 'maximal munch' algorithm, matching only
        the longest strings.

        For example, if 'foot' and 'footwear' are both in the trie,
        then the resulting list will contain footwear, not foot.

        If a character is not found in the trie, the character will
        simply be appended to the list.

        '''
        if self.populated:
            results = list()
            while(string):
                token = self.__next_token(string)
                results.append(token)
                string = string[len(token):]
            return results
        else:
            raise ParserError("Parser not yet populated, must call force_populate() before parsing.")

    def __next_token(self, string):
        '''
        Returns the next valid token.
        '''
        temp = ''
        for c in string:
            temp += c
            if temp in self.trie:
                continue
            elif (temp not in self.trie and
                    temp is c):
                return temp
            elif(temp not in self.trie and
                    temp is not c):
                return temp[:-1]
        return temp
        

    def force_populate(self):
        '''
        Populates the parser with the entire contents of the 
        word_file.
        '''
        with open(self.word_file, 'r') as f:
            for word in f:
                self.trie.add_string(word)
        self.populated = True

