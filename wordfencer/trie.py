import collections.abc
from itertools import zip_longest


class Trie(collections.abc.Container):

    def __init__(self):
        self.root = dict()

    def add_string(self, string):
        current_node = self.root
        for pair in zip_longest(string, string[1:]):
            if (pair[0] not in current_node and
                pair[1] is not None):
                current_node[pair[0]] = { pair[1] : dict() }
            elif (pair[0] not in current_node and
                pair[1] is None):
                current_node[pair[0]] = pair[1]
            current_node = current_node[pair[0]]

    def __contains__(self, seq): 
        current_node = self.root
        try:
            for elem in seq:
                current_node = current_node[elem]
        except KeyError:
            return False
        return True
        
    def find_match(self, string):
        current_node = self.root
        try:
            for c in string:
                current_node = current_node[c]
        except KeyError:
            return False
        return True
