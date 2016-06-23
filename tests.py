import unittest
import parser


class TestParser(unittest.TestCase):


    def test_single_token(self):
        '''
        Passes if dictionary with 'ABC' entry correctly parses
        string 'ABC' into the token list ['ABC'].
        '''
        test_list = ['ABC']
        p = parser.Parser(test_list)
        p.set_wordref(test_list)
        result = p.parse('ABC')
        self.assertEqual(['ABC'], result)


    def test_first_string_match(self):
        '''
        Passes when a dictionary with only an 'ABC' entry
        correctly tokenizes 'ABCDE' into ['ABC', 'D', 'E'].
        '''
    
    

if __name__ == '__main__':
    unittest.main()
