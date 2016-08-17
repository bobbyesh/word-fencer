==========
wordfencer
==========


Copyright (c) 2016 Robert Eshleman

This code is available under the "MIT License". Please see the file LICENSE in 
this distribution for license terms.


This is a Python module for tokenizing natural languages without delimiters.


Supported Languages
===================

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


:Note:  The general parsers ChineseParser (zh) and CantoneseParser (yue) support both simplified and traditional characters.


Installation
============

Install using pip like this:

    $ sudo pip3 install wordfencer


Tarball can found here_.

.. _here: https://pypi.python.org/pypi/wordfencer


Examples
========


Import and instantiate which parser you want to use.  Refer to 
`Supported Languages`_ for the names of all the available parsers and the
langauges they parse.

>>> from wordfencer.parser import ChineseParser
>>> parser = ChineseParser()


The `parse` method returns a list of the input string's subtokens, like this:

>>> parser.parse('真理惟一可靠的标准就是永远自相符合。')
['真理', '惟一', '可靠', '的', '标准', '就是', '永远', '自相', '符合', '。']


You can also get all of the tokens (not just the longest), by setting the
all_combos option to true:

>>> parser.parse('真理惟一可靠的标准就是永远自相符合。', all_combos=True)
{'永远', '符合', '就是', '自相', '靠', '准', '真理', '一', '是', '的', '。',
 '相符', '远', '合', '理', '惟一', '标准', '可靠'}


Using the Factory
-----------------


The `parser_factory` takes a string language tag and returns a parser for that language.
The language tags that the `parser_factory` accepts are standard IETF language tags
defined by the IANA Language Subtag Registry.  See `Supported Languages`_ for the
tags and which languages they refer to.

>>> from wordfencer.parser import parser_factory, ChineseParser
>>> parser = parser_factory('zh')
>>> isinstance(parser, ChineseParser)
True
>>> parser.parse('真理惟一可靠的标准就是永远自相符合。')
['真理', '惟一', '可靠', '的', '标准', '就是', '永远', '自相', '符合', '。']


The extra subtag specifies the script, here is Chinese ("zh") with simplified hanzi 
("Hans").

>>> from wordfencer.parser import parser_factory, ChineseSimplifiedParser
>>> parser = parser_factory('zh-Hans')
>>> isinstance(parser, ChineseSimplifiedParser)
True
>>> parser.parse('真理惟一可靠的标准就是永远自相符合。')
['真理', '惟一', '可靠', '的', '标准', '就是', '永远', '自相', '符合', '。']



The reference dictionaries used for parsing were built using the data from the
CEDICT and YEDICT free dictionaries available through the creative commons
license.

Presentation: https://docs.google.com/presentation/d/1GBE3QqZLmcGwB0RsqxjGvJBBdFKNjn37LCfFjPJg_kM/edit?usp=sharing

Copyright (c) 2016 Robert Eshleman
