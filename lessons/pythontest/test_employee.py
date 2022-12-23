#!/usr/bin/python3

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setupClass")

    @classmethod
    def tearDownClas(cls):
        print("teardownClass")

    def setUp(self):
        print("setUp")
        self.emp_1 = Employee("Jay", "Kay", 50000)
        self.emp_2 = Employee("May", "Hay", 250000)


    def tearDown(self):
        print("tearDown\n")


    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, "Jay.Kay@email.com")
        self.assertEqual(self.emp_2.email, "May.Hay@email.com")

        self.emp_1.first = "Lady"
        self.emp_2.first = "Bee"

        self.assertEqual(self.emp_1.email, "Lady.Kay@email.com")
        self.assertEqual(self.emp_2.email, "Bee.Hay@email.com")


    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, "Kay Jay")
        self.assertEqual(self.emp_2.fullname, "Hay May")

        self.emp_1.first = "Lady"
        self.emp_2.first = "Bee"

        self.assertEqual(self.emp_1.fullname, "Kay Lady")
        self.assertEqual(self.emp_2.fullname, "Hay Bee")


    def test_applyraise(self):
        print("test_payraise")
        self.emp_1.applyraise()
        self.emp_2.applyraise()
        
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 262500)


if __name__ == '__main__':

    unittest.main()
