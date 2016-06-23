# parser.py

'''
This parser will parser any string of text of any language which has no delimiters.
These are languages such as Chinese, Hindi, Thai, etc...
'''

class Parser:


    def __init__(self):
        self.dictionary = self.build_dict()
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

    def build_dict(self):
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

            
            



def main():
    p = Parser()
    print('Dictionary')
    print(p.dictionary)
    print('Result for parsing ABCDE')
    result = p.parse('ABCDE')
    print(result)


if __name__ == '__main__':
    main()
