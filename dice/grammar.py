# The MIT License (MIT)
#
# Copyright (c) 2016 Sean Quinn
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
from dice.tokens import Integer
from pyparsing import (CaselessLiteral, Literal, Optional, StringStart, StringEnd, Word, nums)
#: Empty


def dice():
    token = Optional(integer()) + CaselessLiteral("d") + dice_sides()
    token.setName("dice")
    token.setResultsName("dice")
    return token


def dice_sides():
    token = integer()\
          | CaselessLiteral("fate") \
          | CaselessLiteral("f")
          #| StringStart() + CaselessLiteral("f") + StringEnd() \
          #| StringStart() + CaselessLiteral("fate") + StringEnd()
    token.setResultsName("dice_sides")
    return token


def expression():
    token = Optional(Literal("(")) + term() + Optional(Literal(")"))
    token.setName("expression")
    return token


def flags():

    token = (
        CaselessLiteral("!advantage")
        | CaselessLiteral("!adv")
        | CaselessLiteral("!disadvantage")
        | CaselessLiteral("!dis")
        | CaselessLiteral("!drop")
        | CaselessLiteral("!grow")
        | CaselessLiteral("!keep")
        | CaselessLiteral("!shrink")
        | CaselessLiteral("!take")
    )

    token.setName("flags")
    token.setResultsName("flags")
    return token


def integer():
    token = Word(nums)
    token.setParseAction(Integer.parse)
    token.setName("integer")
    return token


def operator():
    token = Literal("+") | Literal("-") | Literal("/") | Literal("*")
    token.setName("operator")
    token.setResultsName("operator")
    return token


def term():
    """
    """
    token = StringStart() + dice() + StringEnd() \
          | StringStart() + dice() + operator() + integer() + StringEnd() \
          | StringStart() + dice() + flags() + StringEnd() \
          | StringStart() + dice() + flags() + operator() + integer() + StringEnd()
    token.setName("term")
    token.setResultsName("term")
    return token


