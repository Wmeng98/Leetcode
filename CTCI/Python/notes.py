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

'''

Python Mutable Data Types
    Id - unique identifier for object -> points to location in memory
    In python all data stored as object with 3 things: 
        id, type, value
    Mutable Objects (changeable)
        list, dict, set
    Immutable objects:
        Integer, float, string, tuple, bool, frozenset
    
        STRINGS ARE NOT MUTABLE in PYTHON!!!

    Passing arguments   
        [MUTABLE] If a mutable object is called by reference in a function, the original variable may be changed. If you want to avoid changing the original variable, you need to copy it to another variable.
        [IMMUTABLE] When immutable objects are called by reference in a function, its value cannot be changed.

None
    None is not the same as 0, False, or an empty string. None is a data type of its own (NoneType) and only None can be None


Comparing 2 objects in Python
    compare for EQUALITY or IDENTITY
    
    == for equality
    is for identity
    __eq__ to compare 2 class instances
        Even if two class instances have the same attribute values, 
        comparing them using == will return False

        You have to tell python how exactly you want equality be defined. 
        do so by defining a special method __eq__ like this

        NOTE: because two different objects can sometimes compare equal 
        (if not then don't bother overloading it). In this case the return id(self) 
        hash function is BROKEN (EQUAL OBJECTS MUST HASH THE SAME)


List Comprehension
    - List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list
    
    SYNTAX
    - `newlist = [expression for item in iterable if condition == True]`
    - NOTE: The return value is a new list, leaving the old list unchanged

    - NOTE:
        - The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome
        - `newlist = [x if x != "banana" else "orange" for x in fruits]`

DefaultDict
- Defaultdict is a container like dictionaries present in the module collections. Defaultdict is a sub-class of the dict class 
  that returns a dictionary-like object. The functionality of both dictionaries and defualtdict are almost same except for the 
  fact that defualtdict never raises a KeyError. It provides a default value for the key that does not exists.

- from collections import defaultdict

Complexity of "in"
    - Here is the summary for in:

    list - Average: O(n)
    set/dict - Average: O(1), Worst: O(n)

    The O(n) worst case for sets and dicts is very uncommon, but it can happen if __hash__ is implemented poorly. 
    This only happens if everything in your set has the same hash value.


operator.itemgetter
    - dict.items() -> array of tuples

    - Return a callable object that fetches item from its operand using the operand’s __getitem__() method. 
        If multiple items are specified, returns a tuple of lookup values. For example


'''

'''
Sorting

    lists have built-in list.sort() method, modifies list in place
    sorted() function builds a new sorted list from an iterable

    [KEY]
        key param to specify a function (or other callable) to be called on each list prior to 
        making comparisons

            sorted("This is a test string from Andrew".split(), key=str.lower)

        value of the key parameter should be a function (or other callable) that takes a single argument and returns a key to use for sorting purposes
        
        LAMBDAS are a good candidate here!!!

    NOTE: Common pattern is to sort complex objects using some of the objects indices as keys
        
            sorted(student_tuples, key=lambda student: student[2])
            sorted(student_objects, key=lambda student: student.age)

    [OPERATOR MODULE FUNCTIONS]
        The key-function patterns shown above are very common, so Python provides convenience functions to make accessor functions easier and faster

            ***** from operator import itemgetter, attrgetter *****

            sorted(student_tuples, key=itemgetter(2))
            sorted(student_objects, key=attrgetter('age'))

        multiple levels of sorting. For example, to sort by grade then by age

            sorted(student_tuples, key=itemgetter(1,2))
            sorted(student_objects, key=attrgetter('grade', 'age'))
        


'''

