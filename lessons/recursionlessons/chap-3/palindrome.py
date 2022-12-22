def isPalindrome(theString):
    '''
        ======= Detect Palindrome Word or Phrase ======
        This function detects whether a word or phrase is
        palindrome or not
    '''

    if len(theString) == 0 or len(theString) == 1:
        return True
    else:
        head = theString[0]
        middle = theString[1:-1]
        last = theString[-1]

        return head == last and isPalindrome(middle)


#   ==============================================

if __name__ == '__main__':

    done = False

    while not done:
        qtn = input("Enter a word: ")

        if qtn == "":
            done = True
            break
        else:
            ans = isPalindrome(qtn)
            print("{} is palindrome: {}".format(qtn, ans))
