# Python

'''

Note Python 3's int doesn't have a max size (bounded by memory)
    float('inf') is for infinity, guaranteed to be higher than any other int value

range vs. xrange (deprc in python3)
    If you want to write code that will run on both Python 2 and Python 3, use range() as the xrange function is deprecated in Python 3
    range() is faster if iterating over the same sequence multiple times.
    xrange() has to reconstruct the integer object every time, but range() will have real integer objects. (It will always perform worse in terms of memory however)

Python - Pass by Value or Reference
    Neither of these 2 concepts applicable
    Values are sent to functions by means of object reference
    
    Pass-by-object-reference
    Almost everything in Python is an object
    Values passed to functions by object-reference
        If immutable, modified value NOT available outside scope of function

        Mutable objects
            list, dict, set, byte array
        Immutable objects
            int, float, complex, string, tuple, frozen set, bytes


Deque
    Double ended queue (impl probably a DOUBLY LINKED LIST - Bidirectional)
    
    `from collections import deque `

    append(), appendLeft, pop(), popLeft()
    index(ele, beg, end), insert(i,a), remove(), count()

    Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, 
        as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.

'''