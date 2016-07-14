# setup.py
"""This module simply reads a dictionary reference file, builds a Trie, and then pickles it.
"""

from parser import *

def build(class_):
    p = class_()
    p.save()

if __name__ == '__main__':
    build(ChineseSimplifiedParser)
    build(ChineseTraditionalParser)
