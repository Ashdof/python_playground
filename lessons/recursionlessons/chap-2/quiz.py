"""
    ==============  Practice Questions  =====================
    The following are the practice questions of chapter two of the book 
"""

'''
    Q1:
    What is 4! (that is, the factorial of 4)?
    4! = 4 x 3 x 2 1
       = 24
'''
def factorial(n):
    if n < 1:
        return n
    else:
        return n * factorial(n - 1)


'''
    Q2:
    How can you use the factorial of (n – 1) to calculate the factorial of n?
    Ans:
    This can be done in two ways: by iteration and by recursion as demonstrated below
'''
def fac1(n):
    '''recursion'''
    if n < 1:
        return n
    else:
        return n * fac1(n - 1)


def fac2(n):
    '''iterative'''
    rs = 1
    for i in range(1, n):
        rs *= i
    return rs


'''
    Q3:
    What is the critical weakness of the recursive factorial function?
    Ans:
    The critical weakness of the recursive factorial function is the
    risk of a stack overflow. A stack overflow is a programming bug
    whereby the constant function calls without returning grows the
    stack until it exceeds the allocated memory. In Python, the
    recursive depth (allocated memory for recursive function call)
    is 1000 and 10,00 in JavaScript but that depends on the browser
'''


'''
    Q4:
    What are the first five numbers of the Fibonacci sequence?
    Ans:
    0, 1, 1, 2, 3, 5
'''


'''
    Q5:
    What two numbers do you add to get the nth Fibonacci number?
    Ans:
    (n - 1) + (n - 2)
'''


'''
    Q6:
    What is the critical weakness of the recursive Fibonacci function?
    Ans:
    It repeats the same calculation over and over again
'''


'''
    Q7:
    What does an iterative algorithm always use?
    Ans:
    A loop and a stack data structure
'''


'''
    Q8:
    Is it always possible to convert an iterative algorithm into a recursive on
    Ans:
    No
'''


'''
    Q9:
    Is it always possible to convert a recursive algorithm into an iterative one?
    Ans: Yes
'''


'''
    Q10:
    Any recursive algorithm can be performed iteratively by using what two things?
    Ans:
    A loop and a stack data structure
'''


'''
    Q11:
    What three features do programming problems that are suitable to recursive solutions have?
    Ans:
    1. The recursive case is not so deep so as to result in a stack overflow
    2. It has a tree-like data structure
    3. It involves backtracking
'''


'''
    =================== Practice Projects   ==========================
'''

'''
    Q1:
    Iteratively calculate the sum of the integer series from 1 to n. This is sim-
    ilar to the factorial() function, except it performs addition instead of
    multiplication. For example, sumSeries(1) returns 1, sumSeries(2) returns
    3 (that is, 1 + 2), sumSeries(3) returns 6 (that is, 1 + 2 + 3), and so on.
    This function should use a loop instead of recursion.
'''

def sumSeries(n):
    '''iterative approach'''

    ans = 0

    for i in range(n + 1):
        ans += i
    return ans


'''
    Q2:
    Write the recursive form of sumSeries(). This function should use recur-
    sive function calls instead of a loop.
'''

def sumRecursion(n):
    '''recursive approach'''

    if n == 0:
        return 0
    else:
        return n + sumRecursion(n - 1)





#   ===========================================================

if __name__ == '__main__':

    val = int(input("Enter a value: "))
    print("Sum of all numbers up to {} = {}".format(val, sumRecursion(val)))

