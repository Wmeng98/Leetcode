'''

[Hash Tables]

Simple Implementation
    Array of linked lists and a hash code function
    To insert a key:
        1. Compute the keys hash code, 2 diff keys can have same hash, can have infinite # keys and limited ints
        2. Map hash code to an index in the array [hash(key) % array_length]
        3. Store key,value in linked list at this index

        If collisions is high (all key hashes map to same index), worst case runtime is O(n)
        Good impl keeps collisions at minimum -> O(1) lookup

Hash Table with Balanced Binary Search Tree as underlying data structure
    Advantages
        No disadvantage of resizing the array
        Reduce hash collisions - don't mod hash value to get index, resulting in more indices
        Could still handle collisions with a LL?

    Disadvantage
        >>> Takes logN (N -> nodes/buckets in the BST) to find key in the BST

'''



'''

[Strings]

String Builder
    concatenate n strings all of length x
    runtime?
        On each iteration, new copy of string created, 2 strings copied over 
            'sentence = sentence + word'
        first iteration -> x
        second -> 2x
        third -> 3x
        ...

        therfore, x + 2x + 3x + 4x + ... nx
        x(n^2)

StringBuilder avoids problem by creating a resizeable array of all the strings, copy back only when necessary
    Basically like building a list of strings, then joining when done

'''