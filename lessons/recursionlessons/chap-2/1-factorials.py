def iterative_factorial(number):
    """
        Compute factorial by iteration
    """
    product = 1

    for i in range(1, number + 1):
        product *= i

    return product

def recursive_factorial(number):
    """
        Compute factorial by recursion
    """
    if number == 1:
        return 1
    else:
        return number * recursive_factorial(number - 1)

#   ==============  Work Area   =============================

val = int(input("Enter a number: "))
for i in range(1, val):
    print("{}! = {}".format(i, recursive_factorial(i)))
