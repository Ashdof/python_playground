#!/usr/bin/python3

import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(25, 10), 35)
        self.assertEqual(calc.add(-5, 10), 5)
        self.assertEqual(calc.add(-2, -7), -9)

    def test_subtract(self):
        self.assertEqual(calc.subtract(25, 10), 15)
        self.assertEqual(calc.subtract(-5, 10), -15)
        self.assertEqual(calc.subtract(-2, -7), 5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(25, 10), 250)
        self.assertEqual(calc.multiply(-5, 10), -50)
        self.assertEqual(calc.multiply(-2, -7), 14)

    def test_divide(self):
        self.assertEqual(calc.divide(25, 10), 2.5)
        self.assertEqual(calc.divide(-5, 10), -0.5)
        self.assertEqual(calc.divide(-2, -7), 0.2857142857142857)
        self.assertRaises(ValueError, calc.divide, 21, 0)

        """The last line can also be written as ffs; just use one
        option

        with self.assertRaises(ValueError):
            calc.divide(21, 0)
        """



#   ========    Unit Test Area  ===========

if __name__ == '__main__':

    unittest.main()
