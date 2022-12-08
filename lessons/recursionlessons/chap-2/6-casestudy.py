#!/usr/bin/python3

def exponent(base, power):
    rs = 1
    i = 0

    while i < power:
        rs *= base
        i += 1

    return rs


def exponents(base, number):
    rs = 1

    for i in range(number):
        rs *= base 

    return rs

#   ===================

num1 = int(input("Base number: "))

if num1 < 1:
    print("A base number cannot be 1 or less")
else:
    num2 = int(input("Exponent number: "))
    
    ans = exponents(num1, num2)
    print(f'{num1: d} to the power {num2: d} is {ans}')
