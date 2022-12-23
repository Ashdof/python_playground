#!/usr/bin/python3

import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(25, 10), 35)
        self.assertEqual(calc.add(-5, 10), 5)
        self.assertEqual(calc.add(-2, -7), -9)






#   ========    Unit Test Area  ===========

if __name__ == '__main__':

    unittest.main()
