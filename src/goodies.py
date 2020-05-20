from bisect import bisect_left

def binary_search(iterable, value):
    """
    Returns first index of value in sorted iterable
    """
    i = bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1

def read_file(file):
    """
    Yields one line of an open file at a time
    """
    for line in file:
        yield line.rstrip("\n")
