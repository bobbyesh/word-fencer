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
        p = parser_factory('zh-Hans')
        self.assertTrue(type(p) is ChineseSimplifiedParser)


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


class TestParser(unittest.TestCase):


    def test_reference_error(self):
        with self.assertRaises(FileNotFoundError):
            temp = Parser('garbage/path')
    

if __name__ == '__main__':
    unittest.main()
