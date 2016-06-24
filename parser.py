# parser.py

'''
This parser will parse any string of text of any language which has no delimiters.
These are languages such as Chinese, Hindi, Thai, etc...

'''

from trie import Trie
import pickle

class ParserError(Exception):
    pass


def parser_factory(lang):
    class_ = {
            'zh-Hans' : ChineseSimplifiedParser,
            'zh-Hant' : ChineseTraditionalParser,
            'yue-Hans' : CantoneseSimplifiedParser,
            'yue-Hans' : CantoneseTraditionalParser,
            }.get(lang)
    return class_()

class Parser(object):

    def __init__(self):
        self.trie = Trie()
        self.populated = False
        self.ref = None

    def reference(self, ref):
        self.ref = ref

    def parse(self, string):
        if not self.populated:
            raise ParserError('Parser not yet populated, must cal force_populate()')
        results = list()
        while(string):
            token = self.__next_token(string)
            if token:
                results.append(token)
                string = string[len(token):]
            else:
                string = ''
        return results

    def __next_token(self, string):
        temp = ''
        for c in string:
            temp += c
            if temp not in self.trie:
                if len(temp) > 1:
                    return temp[:-1]
                if len(temp) == 1:
                    return temp
        return temp

    def force_populate(self):
        '''
        Populates the parser with the entire contents of the 
        word reference file.
        '''
        if not self.ref:
            raise ParserError('No reference file assigned yet')
        with open(self.ref, 'r') as f:
            for word in f:
                self.trie.add_string(word)
        self.populated = True


class ChineseSimplifiedParser(Parser):
    

    def __init__(self):
        super()
        self.load()
    
    def save(self):
        with open('data/zh-Hans.pickle', 'wb') as f:
            pickle.dump(self.trie, f)

    def load(self):
        with open('data/zh-Hans.pickle', 'rb') as f:
            self.trie = pickle.load(f)
            self.populated = True

class ChineseTraditionalParser(Parser):


    def __init__(self):
        super()

class CantoneseSimplifiedParser(Parser):


    def __init__(self):
        super()

class CantoneseTraditionalParser(Parser):


    def __init__(self):
        super()
