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


#   ============    Work Area   =============

val = int(input("Enter a number: "))
print("Fibonacci of {} = {}".format(val, fibonacci(val)))
