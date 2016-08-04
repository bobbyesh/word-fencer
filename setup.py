# setup.py
"""This module simply reads a dictionary reference file, builds a Trie, and then pickles it.
"""

from distutils.core import setup
setup(
    name = "wordfencer",
    packages = ["wordfencer"],
    version = "1.0",
    description = "Parser for natural languages without space delimiters",
    author = "Bobby Eshleman",
    author_email = "bobbyeshleman@gmail.com", 
    url = "https://github.com/bobbyesh/word-fencer",
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Natural Language :: Cantonese",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: Chinese (Traditional)",
        "Natural Language :: Thai",
    ],
    long_description = """\
Parser For Chinese, Cantonese, and Thai
---------------------------------------

Tokenizes the words found in any arbitrary string in any of the supported languages.
""",
    
)
