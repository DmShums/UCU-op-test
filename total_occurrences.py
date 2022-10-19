from hashlib import sha3_224


def total_occurrences(s1, s2, ch):
    """
    Returns sum of ch's occurrences in s1 and s2.
    >>> total_occurrences('color', 'yellow', 'l')
    3
    >>> total_occurrences('red', 'blue', 'l')
    1
    >>> total_occurrences('green', 'purple', 'b')
    0
    """

    s=s1+s2
    counter = 0
    for i in s:
        if i== ch:
            counter+=1
    return(counter)
if __name__=='__main__':
    import doctest
    doctest.testmod()
