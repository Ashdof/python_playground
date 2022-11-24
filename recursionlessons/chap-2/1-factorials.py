def factorial(number):
    product = 1

    for i in range(1, number + 1):
        product *= i

    return product


#   ==============  Work Area   =============================

val = int(input("Enter a number: "))
for i in range(1, val):
    print("{}! = {}".format(i, factorial(i)))
