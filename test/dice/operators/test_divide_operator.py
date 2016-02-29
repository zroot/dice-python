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
from dice.operators import Divide
import unittest


class DivideOperatorTest(unittest.TestCase):
    """
    """

    def test_init(self):
        #: TBW
        #:
        #: Given
        #: When
        #: Then
        operator = Divide(5, 1)
        self.assertEqual(operator.original_operands, (5,1))
        self.assertEqual(operator.operands, (5,1))

    def test_repr(self):
        #: Test that the string representation of the operator is what is
        #: expected.
        #:
        #: Given an instance of the Divide operator on operands 6 and 2
        #: When the method __repr__ is called
        #: Then the result should be "Divide(6, 2)"
        operator = Divide(6, 2)
        self.assertEqual("Divide(6, 2)", str(operator))

    def test_evaluate(self):
        #: Test that the evaluation of the operator is correct.
        #:
        #: Given an instance of the Divide operator on operands 6 and 2
        #: When the operator is evaluated
        #: Then the result should be 3.
        operator = Divide(6, 2)
        actual = operator.evaluate()
        self.assertEqual(actual, 3)

    def test_evaluate_divide_by_zero(self):
        #: Test that the evaluation of the operator results in a
        #: divide-by-zero error being raised.
        #:
        #: Given an instance of the Subtract operator on operands 6 and 0
        #: When the operator is evaluated
        #: Then a ZeroDivisionError is raised
        with self.assertRaises(ZeroDivisionError):
            operator = Divide(6, 0)
            actual = operator.evaluate()

    def test_evaluate_invalid(self):
        #: Test that the evaluation of the operator raises a ValueError
        #: when an invalid term is supplied.
        #:
        #: Given an instance of the Divide operator on operands 6 and
        #:     "invalid"
        #: When the operator is evaluated
        #: Then a ValueError should be raised.
        with self.assertRaises(ValueError):
            operator = Divide(6, "invalid")
            actual = operator.evaluate()

    def test_evaluate_operand_as_integral_string(self):
        #: Test that the evaluation of the operator is correct on all
        #: numeric operands, even if one of those operands is represtend
        #: as a string.
        #:
        #: Given an instance of the Subtract operator on operands 6 and "3"
        #: When the operator is evaluated
        #: Then the result should be 7.
        operator = Divide(6, "3")
        actual = operator.evaluate()
        self.assertEqual(actual, 2)

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
        #operator = Divide()
        #operator.function()
        pass


if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromTestCase(DivideOperatorTest)
    suite = unittest.TestSuite(tests)

    unittest.TextTestRunner(descriptions=True, verbosity=5).run(suite)
