#!/usr/bin/python3
"""Python Doctest"""

import collections

def group_by_length(words):
    """Group words

    Description:
        This function groups words into sets by the length of each word

    Arguments:
        words (list): a list of words with varying length

    Returns:
        a dictionary grouping words into sets by length

    #========   Test Section    ========================
    
    >>> grouped = group_by_length(['python', 'module', 'of', 'the', 'week'])
    >>> grouped
    defaultdict(<class 'set'>, {6: {'python', 'module'}, 2: {'of'}, 3: {'the'}, 4: {'week'}})

    >>> asem = [23, 'is', 'all over', 'the', 'most', 'interesting', 8756, 'coded', 'platform']
    >>> rs = group_by_length(asem)
    Traceback (most recent call last):
        ...
    TypeError: object of type 'int' has no len()

    """
    d = collections.defaultdict(set)
    for word in words:
        d[len(word)].add(word)

    return d



#   =============================================================

if __name__ == '__main__':
    import doctest

    doctest.testmod()
