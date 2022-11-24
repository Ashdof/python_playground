def fibonacci(number):
    """
        Compute the fibonacci by iteration
    """
    a, b = 1, 1
    print('a = %s, b = %s' % (a, b))

    for i in range(1, number):
        a, b = b, a + b     #get the next fibonacci number
        print('a = %s, b = %s' % (a, b))

    return a

def recursive_fibonacci(number):
    """
        Compute fibonacci by recursion. Much of the code is for displaying the output;
        particularly how the code is executing
    """
    print("recursive_fibonacci(%s) called" % (number))

    if number == 1 or number == 2:
        #base case
        print("recursive_fibonacci(%s) returning 1" % (number))
        return 1
    else:
        # recursive case
        print("Calling recursive_fibonacci(%s) and recursive_fibonacci(%s)" % (number - 1, number - 2))
        rs = recursive_fibonacci(number - 1) + recursive_fibonacci(number - 2)
        print("Call to recursive_fibonacci(%s) returning %s", (number, rs))
        return rs

#   ============    Work Area   =============

val = int(input("Enter a number: "))
print("Fibonacci of {} = {}".format(val, recursive_fibonacci(val)))
