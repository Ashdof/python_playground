callstack = []  # the call stack which holds the frame objects
callstack.append({'returnAddr': 'start', 'number': 5})
returnVal = None

while len(callstack) > 0:
    # the body of the factorial function

    number = callstack[-1]['number']
    returnAddr = callstack[-1]['returnAddr']

    if returnAddr == 'start':
        if number == 1:

            #base case
            returnVal = 1
            callstack.pop()  # return from function call
            continue
        else:

            # recursive case
            callstack[-1]['returnAddr'] = 'after recursive call'
            callstack.append({'returnAddr': 'start', 'number': number - 1})
            continue

    elif returnAddr == 'after recursive call':
        returnVal = number * returnVal
        callstack.pop()
        continue

print(returnVal)
