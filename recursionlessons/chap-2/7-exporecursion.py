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
                ans = exporecursion(int(base), int(expo))
                print(f'{base} raised to the power {expo} is {ans}')
