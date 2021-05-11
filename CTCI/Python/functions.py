'''

Python Inner/Nested Functions
    #  Has access to variables and names defined in the enclosing function
    #  Encapsulation, hide from external access

In Python, Functions are **first-class citizens**
    Means on par with any other object such as numbers, strings, lists, tuples, modules, etc.
    You can dynamically create or destroy them, store them in data structures, pass them as arguments to other functions, use them as return values, and so forth.

    - can be stored in variables and data structures
    - can be passed as a parameter to a subroutine
    - can be returned as the result of a subroutine
    - can be constructed at runtime
    - has intrinsic identity (independent of any given name)


'''

# Closure Factory Functions
# NOTE: Higher-order functions are functions that operate on other functions by taking them as arguments, returning them, or both

# Closures are dynamically created functions that are returned by other functions. 
# Their main feature is that they have full access to the variables and names defined in the local namespace (SNAPSHOT) where the closure was created

# powers.py
def generate_power(exponent):
    def power(base):
        return base ** exponent
    return power