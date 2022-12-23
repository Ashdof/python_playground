#!/usr/bin/python3

class Employee:
    """ A simple employee class """

    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.last, self.first)

    def applyraise(self):
        self.pay = int(self.pay * raise_amount)
