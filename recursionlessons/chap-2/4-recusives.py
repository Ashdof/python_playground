print('Code in a loop')
i = 1

while i < 5:
    print(i, 'Hello, World!')
    i += 1

print('\nCode in function')
def hello(i = 0):
    """
        code in a recusive function
    """
    print(i, 'Hello, World!')

    i += 1
    if i < 5:
        # recursive case
        hello(i)
    else:
        return

#   ========    Work Area   ================

hello()
