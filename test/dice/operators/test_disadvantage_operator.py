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
from dice.operators import Disadvantage
import unittest


class DisadvantageOperatorTest(unittest.TestCase):
    """
    """

    def test_init(self):
        #: TBW
        #:
        #: Given
        #: When
        #: Then
        operator = Disadvantage(5, 1)
        self.assertEqual(operator.original_operands, (5,1))
        self.assertEqual(operator.operands, (5,1))

    def test_repr(self):
        #: Test that the string representation of the operator is what is
        #: expected.
        #:
        #: Given an instance of the Disdvantage operator on operands
        #: When the method __repr__ is called
        #: Then the result should be "Disdvantage"
        operator = Disadvantage(5, 1)
        self.assertEqual("Disadvantage(5, 1)", str(operator))

    def test_evaluate(self):
        #: TBW
        #:
        #: Given
        #: When
        #: Then
        pass

    def test_evaluate_object(self):
        #: TBW
        #:
        #: Given
        #: When
        #: Then
        pass

    def test_function(self):
        #: TBW
        #:
        #: Given
        #: When
        #: Then
        #operator = Disadvantage()
        #operator.function()
        pass


if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromTestCase(DisadvantageOperatorTest)
    suite = unittest.TestSuite(tests)

    unittest.TextTestRunner(descriptions=True, verbosity=5).run(suite)
