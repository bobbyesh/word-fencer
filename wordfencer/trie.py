# trie.py
"""
Copyright (c) 2016 Robert Eshleman
This code is available under the "MIT License". Please see the file LICENSE in 
this distribution for license terms.

"""

import collections.abc
from itertools import zip_longest
import pdb


class Node:
    def __init__(self):
        self.children = dict()


class Trie(collections.abc.Container):

    def __init__(self):
        self.root = dict()

    def add_string(self, string):
        current_node = self.root
        for current, next in zip_longest(string, string[1:]):

            if current_node is None:
                return
            # Check that the current character is not in the current node, otherwise
            # each definition will cut the previous child branch off the tree
            if current not in current_node:
                if next is not None:
                    current_node[current] = { next: None }
                else:
                    current_node[current] = None

            current_node = current_node[current]

    def __contains__(self, seq):
        current_node = self.root
        try:
            for elem in seq:
                if current_node is None:
                    return False
                current_node = current_node[elem]
        except KeyError:
            return False
        '''
        print('Segment::::: ' + seq)
        print('++++++++++++++')
        import json
        json_string = json.dumps(current_node, sort_keys=True, indent=4, ensure_ascii=False)
        print(json_string)
        print('++++++++++++++')
        '''
        return True
