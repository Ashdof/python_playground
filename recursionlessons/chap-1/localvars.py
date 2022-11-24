def a():
    spam = 'Ant'
    print('Spam is ' + spam)
    b()
    print('Spam is ' + spam)

def b():
    spam = 'Bobcat'
    print('Spam is ' + spam)
    c()
    print('Spam is ' + spam)

def c():
    spam = 'Coyote'
    print('Spam is ' + spam)



#   =============================================

if __name__ == '__main__':

    a()
