# tests.py
"""Defines tests for :class:`Trie`, :class:`Parser`, :func:`parser_factory`.

"""


import unittest
import parser
from parser import *
import trie


class TestTrie(unittest.TestCase):

    def test_one_entry(self):
        t = trie.Trie()
        t.add_string('ABC')
        self.assertTrue('ABC' in t)
        self.assertTrue(t.root == {'A' : {'B': {'C': None}}})

    def test_two_entry(self):
        t = trie.Trie()
        t.add_string('ABC')
        t.add_string('Axx')
        self.assertTrue('ABC' in t)

    def test_same_first_middle(self):
        t = trie.Trie()
        t.add_string('ABC')
        t.add_string('ABX')
        self.assertTrue('ABC' in t)
        self.assertTrue('ABX' in t)

    def test_different_first(self):
        t = trie.Trie()
        t.add_string('ABC')
        t.add_string('ZBC')
        self.assertTrue('ABC' in t)
        self.assertTrue('ZBC' in t)

    def test_no_match_first(self):
        t = trie.Trie()
        t.add_string('ABC')
        self.assertFalse('?BC' in t)

    def test_no_match_mid(self):
        t = trie.Trie()
        t.add_string('ABC')
        self.assertFalse('A?C' in t)

    def test_no_match_last(self):
        t = trie.Trie()
        t.add_string('ABC')
        self.assertFalse('AB?' in t)

    def test_different_end(self):
        t = trie.Trie()
        t.add_string('ABC')
        t.add_string('ABX')
        self.assertFalse('AB?' in t)


class TestParserFactory(unittest.TestCase):


    def test_chinese_simplified(self):
        zh_Hans = parser_factory('zh-Hans')
        zh_Hant = parser_factory('zh-Hant')
        yue_Hans = parser_factory('yue-Hans')
        yue_Hant = parser_factory('yue-Hant')
        self.assertTrue(type(zh_Hans) is ChineseSimplifiedParser)
        self.assertTrue(type(zh_Hant) is ChineseTraditionalParser)
        self.assertTrue(type(yue_Hans) is CantoneseSimplifiedParser)
        self.assertTrue(type(yue_Hant) is CantoneseTraditionalParser)

class TestParserBaseClass(object):
    """Abstract base class for testing parsers."""

    def setUp(self):
        self.p = self.parser()
    
    def test_multiple_tokens(self):
        string = ''.join(x for x in self.tokens)
        result = self.p.parse(string)
        self.assertEqual(set(result), self.tokens)

    def test_empty_str(self):
        self.assertEqual(self.p.parse(''), [])


class TestChineseSimplifiedParser(unittest.TestCase):


    def setUp(self):
        self.p = ChineseSimplifiedParser()

    def test_single_token(self):
        result = self.p.parse('感')
        self.assertEqual(['感'], result)


    def test_first_string_match(self):
        result = self.p.parse('感?')
        self.assertEqual(['感','?'], result)

    def test_two_word_sequence(self):
       result = self.p.parse('政府感同身受')
       self.assertEqual(['政府', '感同身受'], result)

    def test_two_similar_words(self):
       result = self.p.parse('非政府政府')
       self.assertEqual(['非政府', '政府'], result)

    def test_matches_and_nonmatches_mixed(self):
       result = self.p.parse('受非政府盈政府')
       self.assertEqual(['受','非政府', '盈','政府'], result)

    def test_random(self):
        self.assertTrue('感' in self.p.trie)


class TestChineseParser(TestParserBaseClass, unittest.TestCase):
    """Define unique tokens in a set, the parser, and the TestParserBaseClass will automatically test
    the parser's functionality.  Tests that ChineseParser parses simplfiied
    and traditional characters.
    """

    tokens = {'鳳凰古城', '鮮明', '鬧翻', '非政府','感同身受'}
    parser = ChineseParser



class TestChineseTraditionalParser(TestParserBaseClass, unittest.TestCase):
    """Define unique tokens in a set, the parser, and the TestParserBaseClass will automatically test
    the parser's functionality.
    """

    tokens = {'鳳凰古城', '鮮明', '鬧翻'}
    parser = ChineseTraditionalParser


class TestCantoneseParser(TestParserBaseClass, unittest.TestCase):
    tokens = {'三八线', '不避艰险', '中国光大银行', '不計其數', '二鬼子', '人頭'}
    parser = CantoneseParser


class TestCantoneseSimplifiedParser(TestParserBaseClass, unittest.TestCase):
    tokens = {'三八线', '不避艰险', '中国光大银行'}
    parser = CantoneseSimplifiedParser


class TestCantoneseTraditionalParser(TestParserBaseClass, unittest.TestCase):
    tokens = {'不計其數', '二鬼子', '人頭'}
    parser = CantoneseTraditionalParser


class TestThaiParser(TestParserBaseClass, unittest.TestCase):
    tokens = {'รูปสี่เหลี่ยมขนมเปียกปูน', 'ทิ้งลูกทิ้งเมีย', 'ผู้ที่สูงอายุ'}
    parser = ThaiParser


class TestParser(unittest.TestCase):


    def test_reference_error(self):
        with self.assertRaises(FileNotFoundError):
            temp = Parser('garbage/path')
    

if __name__ == '__main__':
    unittest.main()
