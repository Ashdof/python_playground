#!/usr/bin/python3

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee("Jay", "Kay", 50000)
        emp_2 = Employee("May", "Hay", 250000)

        self.assertEqual(emp_1.email, "Jay.Kay@email.com")
        self.assertEqual(emp_2.email, "May.Hay@email.com")

        emp_1.first = "Lady"
        emp_2.first = "Bee"

        self.assertEqual(emp_1.email, "Lady.Kay@email.com")
        self.assertEqual(emp_2.email, "Bee.Hay@email.com")


    def test_fullname(self):

        emp_1 = Employee("Jay", "Kay", 50000)
        emp_2 = Employee("May", "Hay", 250000)

        self.assertEqual(emp_1.fullname, "Kay Jay")
        self.assertEqual(emp_2.fullname, "Hay May")

        emp_1.first = "Lady"
        emp_2.first = "Bee"

        self.assertEqual(emp_1.email, "Kay Lady")
        self.assertEqual(emp_2.email, "Hay Bee")


    def test_applyraise(self):

        emp_1 = Employee("Jay", "Kay", 50000)
        emp_2 = Employee("May", "Hay", 250000)

        emp_1.applyraise()
        emp_2.applyraise()
        
        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_1.pay, 262500)


if __name__ == '__main__':

    unittest.main()
