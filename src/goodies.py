from bisect import bisect_left
from collections import deque

def binary_search(iterable, value):
    """
    Returns first index of value in sorted iterable
    """
    i = bisect_left(iterable, value)
    if i < len(iterable) and iterable[i] == value:
        return i
    else:
        return -1

def read_file(file):
    """
    Yields one line of an open file at a time
    """
    for line in file:
        yield line.rstrip("\n")

def type_as_str(x) -> str:
    """
    Returns the type of x as a nice string
    """
    return str(type(x))[8:-2]


class Queue(deque):

    def __init__(self, iterable = []):
        deque.__init__(self, iterable)

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(list(self))})"

    def enqueue(self, item):
        self.append(item)

    def dequeue(self):
        return self.popleft()

    def peek(self):
        answer = self.dequeue()
        self.appendleft(answer)
        return answer

    
class Stack:

    def __init__(self, iterable = []):
        self.deque = deque(iterable)

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(list(self))})"

    def enqueue(self, item):
        self.append(item)

    def dequeue(self):
        return self.popleft()

    def peek(self):
        answer = self.dequeue()
        self.appendleft(answer)
        return answer
