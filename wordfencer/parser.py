# parser.py
"""
Copyright (c) 2016 Robert Eshleman
This code is available under the "MIT License". Please see the file LICENSE in
this distribution for license terms.


This module provides classes for parsing strings of natural languages
that do not use space delimiters.


Currently Supported Languages
=============================

====================== ============= ==========================
Language               Language Code Parser Class
====================== ============= ==========================
Mandarin               zh            ChineseParser
Mandarin Simplified    zh-Hans       ChineseSimplifiedParser
Mandarin Traditional   zh-Hant       ChineseTraditionalParser
Cantonese              yue           CantoneseParser
Cantonese Simplified   yue-Hans      CantoneseSimplifiedParser
Cantonese Traditional  yue-Hant      CantoneseTraditionalParser
Thai                   th or thai    ThaiParser
====================== ============= ==========================


"""

import os
import pickle


def is_cjk_punctuation(char):
    """Returns true if char is a punctuation mark in a CJK language."""
    lower = int('0x3000', 16)
    higher = int('0x300F', 16)
    return ord(char) >= lower and ord(char) <= higher


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
            'zh' : ChineseParser,
            'yue-Hans' : CantoneseSimplifiedParser,
            'yue-Hant' : CantoneseTraditionalParser,
            'yue' : CantoneseParser,
            'thai' : ThaiParser,
            'th' : ThaiParser,
            }.get(lang)
    return class_()


class Parser(object):

    """Defines a generic class for parsing languages with no space delimiters.

    `Parser` uses a pre-existing reference dictionary to build a Trie.
    :func:`force_populate` builds the set out of the reference dictionary file.
    :func:`parse` returns a list of words parsed from :arg:`string`.  The longest
    segment is always selected.


    Attributes
    ==========

    db : set
        The data structure used to perform parsing algorithm.
    populated : boolean
        True if the db has already been populated with words, otherwise False.
    ref : string
        The relative path to the reference dictionary file.
    file : string
        The relative path to the pickle file holding a previously built set.


    """

    def __init__(self, name):
        self.ref = os.path.dirname(__file__) + '/data/' + name + '.txt'
        self.file = os.path.dirname(__file__) + '/data/' + name + '.pickle'
        self.db = set()
        self.populated = False
        self.load()

    def parse(self, string, all_combos=False):
        """Returns a list of words created from segmenting :arg:`string`.

        ..note:  When a series of characters could match a shorter dictionary entry or
        longer entry, the longer one is always selected.
        """
        if not all_combos:
            return self.default_parse(string)
        else:
            return self.all_combinations(string)


    def default_parse(self, string):
        """Returns a list of words created from segmenting :arg:`string`.

        ..note:  When a series of characters could match a shorter dictionary entry or
        longer entry, the longer one is always selected.
        """
        results = list()
        while(string):
            token = self.longest(string)
            results.append(token)
            string = string[len(token):]
        return results

    def longest(self, string):
        if len(string) == 1:
            return string
        result = string[0]
        temp = result
        for c in string[1:]:
            temp += c
            if temp in self.db:
                result = temp
        return result

    def all_combinations(self, string):
        token_set = set()
        for i in range(len(string)):
            for elem in self.default_parse(string[i:]):
                token_set.add(elem)
        return token_set

    def load(self):
        try:
            with open(self.file, 'rb') as f:
                self.db = pickle.load(f)
                self.populated = True
        except FileNotFoundError:
            self.force_populate()
            self.save()

    def force_populate(self):
        """
        Populates the parser with the entire contents of the
        word reference file.
        """
        if not os.path.exists(self.ref):
            raise FileNotFoundError("The reference file path '{}' does not exists.".format(self.ref))
        with open(self.ref, 'r') as f:
            for word in f:
                word = word.strip('\n')
                self.db.add(word)
        self.populated = True

    def save(self):
        with open(self.file, 'wb') as f:
            pickle.dump(self.db, f)


class ChineseParser(Parser):
    """This parser is for Mandarin Chinese written with Simplified OR Traditional characters.

    """

    def __init__(self):
        super().__init__('zh')


class ChineseSimplifiedParser(Parser):
    """This parser is for Mandarin Chinese written with Simplified characters.

    """

    def __init__(self):
        super().__init__('zh-Hans')


class ChineseTraditionalParser(Parser):
    """This parser is for Mandarin Chinese written with Traditional characters.

    All attributes and functionality inherited from :class:`Parser`.

    """

    def __init__(self):
        super().__init__('zh-Hant')


class CantoneseParser(Parser):
    """This parser is for Cantonese written with Simplified OR Traditional characters.

    """

    def __init__(self):
        super().__init__('yue')


class CantoneseSimplifiedParser(Parser):
    """This parser is for Cantonese written with Simplified characters.

    All attributes and functionality inherited from :class:`Parser`.


    """

    def __init__(self):
        super().__init__('yue-Hans')


class CantoneseTraditionalParser(Parser):
    """This parser is for Cantonese written with Traditional characters.

    All attributes and functionality inherited from :class:`Parser`.


    """

    def __init__(self):
        super().__init__('yue-Hant')


class ThaiParser(Parser):
    """This parser is for Thai.

    All attributes and functionality inherited from :class:`Parser`.


    """

    def __init__(self):
        super().__init__('thai')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
