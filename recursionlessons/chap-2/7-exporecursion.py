#!/usr/bin/python3

def exporecursion(base, exponent):
    """Compute for the value of base to the power exponent"""

    if exponent == 1:
        # base case
        return base
    elif exponent % 2 == 0:
        # recursive case, when exponent is even
        ans = exporecursion(base, exponent // 2)
        return ans * ans
    elif exponent % 2 == 1:
        # recursive case, when exponent is odd
        ans = exporecursion(base, exponent // 2)
        return ans * ans * base


def expobypowerrule(base, exponent):
    '''iCompute for the power of a number by the power rule that recursive algorithms uses'''

    # step 1 - determine the operation to perform
    opstack = []
    
    while exponent > 1:
        if exponent % 2 == 0:
            # exponent is even
            
            opstack.append('square')
            exponent = exponent // 2
        elif exponent % 2 == 1:
            # exponent is odd
            
            exponent -= 1
            opstack.append('mutliply')

    # step 2 - perform operation in reverse order

    ans = base  # start ans at 'base'
    while opstack:
        op = opstack.pop()

        if op == 'multiply':
            ans *= base
        elif op == 'square':
            ans *= ans

    return ans


#   ============================================

if __name__ == '__main__':

    done = False

    while not done:
        base = input('Enter base value: ')

        if base == '':
            done = True
            break
        else:
            expo = input('Enter exponent value: ')
            if expo == '':
                done = True
                break
            else:
                ans = expobypowerrule(int(base), int(expo))
                print(f'{base} raised to the power {expo} is {ans}')
