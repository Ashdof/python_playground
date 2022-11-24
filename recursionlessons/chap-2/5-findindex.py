def findindex_iterative(word, string):
    """
        This function finds the index at which word appears in string. 
        It uses iterative approach to find the index.
    """

    i = 0
    while i < len(string):
        if string[i:i + len(word)] == word:
            return i    # word found
        i += 1

    return -1   # word not found

def findindex_recursive(word, string, i = 0):
    """
        This function finds the index at which word appears in string.
        It uses recusive approach to find the index
    """
    if i >= len(string):
        return -1   # base case, word not found

    if string[i:i + len(word)] == word:
        return i    # base case, word found
    else:
        #   recursive case
        return findindex_recursive(word, string, i + 1)


#   ==========  Work Area   ==================================

if __name__ == '__main__':
    val1 = input("Enter word: ")
    val2 = input("Enter sentence: ")
    val3 = findindex_iterative(val1, val2)

    if val3 == -1:
        print("Sorry, {} was not found".format(val1))
    else:
        print('Found {} at position {}'.format(val1, findindex_iterative(val1, val2)))
        print('Found {} at position {}'.format(val1, findindex_recursive(val1, val2)))
