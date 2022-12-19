#!/usr/bin/python3

def rev(theString):

    if len(theString) == 0 or len(theString) == 1:
        return theString
    else:
        head = theString[0]
        tail = theString[1:]

        return rev(tail) + head


#   ====================================

if __name__ == '__main__':

    done = False

    while not done:
        qtn = input("Enter a word: ")
        if qtn == "":
            done = True
            break
        else:
            ans = rev(qtn)
            print("Reversed: {}".format(ans))
