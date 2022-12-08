def factorial(number):
    product = 1

    for i in range(1, number + 1):
        product *= i

    return product

def recursive_factorial(number):
    
    # base case
    if number == 1:
        return 1
    else:
        #recursive case
        return number * recursive_factorial(number - 1)

def fibonacci(number):
    a, b = 1, 1
    print("a = %s, b = %s" % (a, b))

    for i in range(1, number):
        a, b = b, a + b # get the next fibonacci number
        print("a = %s, b = %s" % (a, b))

    return a

def recursive_fibonacci(number):
    print("Fibonacci(%s)called." % number)

    if number == 1 or number == 2:
        print("Call to fibonacci(%s) returning 1" % (number))
        return 1
    else:
        print("Calling fibonacci(%s) and fibonacci(%s)" % (number - 1, number - 2))
        result = recursive_fibonacci(number - 1) + recursive_fibonacci(number - 2)
        print("Call to fibonacci(%s) returning %s" % (number, result))

        return result

def rec_fibo(number):
    if number == 1 or number == 2:
        return 1
    else:
        rs = rec_fibo(number - 1) + rec_fibo(number - 2)
        print(number, ' - ', rs)

        return rs

#   ==================================

if __name__ == '__main__':
    val = int(input("Enter a number: "))
    print(rec_fibo(val))
