import unittest
import parser


class TestTrie(unittest.TestCase):

    def test_one_entry(self):
        trie = parser.Trie()
        trie.add_string('ABC')
        self.assertTrue('ABC' in trie)
        self.assertTrue(trie.root == {'A' : {'B': {'C': None}}})

    def test_two_entry(self):
        '''
        Trie matches 'ABC' after adding 'ABC' and 'Axx'.
        '''
        trie = parser.Trie()
        trie.add_string('ABC')
        trie.add_string('Axx')
        self.assertTrue('ABC' in trie)

    def test_same_first_middle(self):
        trie = parser.Trie()
        trie.add_string('ABC')
        trie.add_string('ABX')
        self.assertTrue('ABC' in trie)
        self.assertTrue('ABX' in trie)

    def test_different_first(self):
        trie = parser.Trie()
        trie.add_string('ABC')
        trie.add_string('ZBC')
        self.assertTrue('ABC' in trie)
        self.assertTrue('ZBC' in trie)

    def test_no_match_first(self):
        trie = parser.Trie()
        trie.add_string('ABC')
        self.assertFalse('?BC' in trie)

    def test_no_match_mid(self):
        trie = parser.Trie()
        trie.add_string('ABC')
        self.assertFalse('A?C' in trie)

    def test_no_match_last(self):
        trie = parser.Trie()
        trie.add_string('ABC')
        self.assertFalse('AB?' in trie)

    def test_different_end(self):
        trie = parser.Trie()
        trie.add_string('ABC')
        trie.add_string('ABX')
        self.assertFalse('AB?' in trie)

class TestParser(unittest.TestCase):


    def test_single_token(self):
        '''
        Passes if dictionary with 'ABC' entry correctly parses
        string 'ABC' into the token list ['ABC'].
        '''
        test_list = ['ABC']
        p = parser.Parser(test_list)
        result = p.parse('ABC')
        self.assertEqual(['ABC'], result)


    def test_first_string_match(self):
        '''
        Passes when a dictionary with only an 'ABC' entry
        correctly tokenizes 'ABCDE' into ['ABC', 'D', 'E'].
        '''
        p = parser.Parser(['ABC'])
        result = p.parse('ABCDE')
    
    

if __name__ == '__main__':
    unittest.main()
