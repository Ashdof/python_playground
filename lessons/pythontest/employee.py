#!/usr/bin/python3

class Employee:
    """ A simple employee class """

    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.__first = first
        self.__last = last
        self.__pay = pay

    @property
    def email(self):
        return "{}.{}@email.com".format(self.__first, self.__last)

    @property
    def fullname(self):
        return "{} {}".format(self.__last, self.__first)

    def applyraise(self):
        self.__pay = int(self.__pay * raise_amount)
