# parser.py
"""This module provides classes for parsing strings of natural languages
that do not use space delimiters.


Currently Supported Languages
=============================
            
====================== ============= ==========================
Language               Language Code Parser Class
====================== ============= ==========================
Mandarin Simplified    zh-Hans       ChineseSimplifiedParser
Mandarin Traditional   zh-Hant       ChineseTraditionalParser
Cantonese Simplified   yue-Hans      CantoneseSimplifiedParser
Cantonese Traditional  yue-Hant      CantoneseTraditionalParser
====================== ============= ==========================

..todo:
    Implement all parsers besides Mandarin Simplified.

"""

import pickle
from trie import Trie
from exceptions import ParserError

def parser_factory(lang):
    """Returns a Parser object specific to the language specified by :param:`lang`.

    :param lang: A string naming the desired parser.  See the keys in :var:`class_`
    for valid strings.

    :Example:

    >>> chinese_parser = parser_factory('zh-Hans')
    >>> isinstance(chinese_parser, ChineseSimplifiedParser)
    True

    >>> cantonese_parser = parser_factory('yue-Hant')
    >>> isinstance(cantonese_parser, CantoneseTraditionalParser)
    True

    """

    class_ = {
            'zh-Hans' : ChineseSimplifiedParser,
            'zh-Hant' : ChineseTraditionalParser,
            'yue-Hans' : CantoneseSimplifiedParser,
            'yue-Hant' : CantoneseTraditionalParser,
            }.get(lang)
    return class_()

class Parser(object):
    """Defines a generic class for parsing languages with no space delimiters.

    `Parser` uses a pre-existing reference dictionary to build a Trie.  
    :func:`reference` sets the reference dictionary to a filename.
    :func:`force_populate` builds the trie out of the reference dictionary file.
    :func:`parse` returns a list of words parsed from :arg:`string`.  The longest
    segment is always selected.


    """

    def __init__(self):
        self.trie = Trie()
        self.populated = False
        self.ref = None

    def reference(self, ref):
        """Sets the reference dictionary file.
    
        ..note:

            The reference file must be a utf-8 text file with one word per line.

        """
        self.ref = ref

    def parse(self, string):
        """Returns a list of words created from segmenting :arg:`string`.
        
        ..note:  When a series of characters could match a shorter dictionary entry or
        longer entry, the longer one is always selected.
        """
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
        """Returns the next token from the :arg:`string`.
        """
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
        """
        Populates the parser with the entire contents of the 
        word reference file.
        """
        if not self.ref:
            raise ParserError('No reference file assigned yet')
        with open(self.ref, 'r') as f:
            for word in f:
                self.trie.add_string(word)
        self.populated = True


class ChineseSimplifiedParser(Parser):
    """This parser is for Mandarin Chinese written with Simplified Characters.

    """

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
    """This parser is for Mandarin Chinese written with Traditional Characters.

    See :class:`Parser` for functionality.

    """

    def __init__(self):
        super()
    
    def save(self):
        with open('data/zh-Hant.pickle', 'wb') as f:
            pickle.dump(self.trie, f)

    def load(self):
        with open('data/zh-Hant.pickle', 'rb') as f:
            self.trie = pickle.load(f)
            self.populated = True

class CantoneseSimplifiedParser(Parser):
    """This parser is for Cantonese written with Simplified Characters.

    See :class:`Parser` for functionality.

    ..todo: Implement this class.

    """

    def __init__(self):
        super()

class CantoneseTraditionalParser(Parser):
    """This parser is for Cantonese written with Traditional Characters.

    See :class:`Parser` for functionality.

    ..todo: Implement this class.

    """

    def __init__(self):
        super()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
