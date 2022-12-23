#!/usr/bin/python3

import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        rs = calc.add(25, 10)
        self.assertEqual(rs, 35)
