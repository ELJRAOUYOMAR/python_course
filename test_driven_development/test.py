


def add(x, y):
    '''
    Add two numbers

    Usage:
    >>> add(8,1)
    9
    >>> add(1,1)
    2
    ''' 
    return x + y


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)