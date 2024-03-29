'''
List vs. Array

List
  Builtin, hold collection of items
  Ordered, Mutable, Indexed Seqeuence of non-unique objects

Array: 
  Need to be explicitly imported either via array module or numpy pkg

Difference:
  - Arrays need to be declared
  - Arrays great for numerical operations (np.array/3 -> simple to divide each el of array)

'''

'''

Note Python 3's int doesn't have a max size (bounded by memory)
float('inf') is for infinity, guaranteed to be higher than any other int value

range vs. xrange (deprc in python3)
If you want to write code that will run on both Python 2 and Python 3, use range() as the xrange function is deprecated in Python 3
range() is faster if iterating over the same sequence multiple times.
xrange() has to reconstruct the integer object every time, but range() will have real integer objects. (It will always perform worse in terms of memory however)

'''

inf = float('inf')

# Second minimum element of an array
# Sol'n: Scan twice, first to find min, second to find next min
#        Can also be done in one for loop
def secondMin(arr):
    
    # Consider base cases arr.len < 2
    
    first = float('inf')
    second = first

    for a in arr:
        if a < first:
            # Found min so far, update first and second
            second = first # first now becomes second smallest so far
            first = a
        elif a < second and a != first:
            # Update second
            second = a
    return second

print('secondMin:', secondMin([10,23,12,15]))




# First non-repeating integers in an array
# Simple sol'n 2 for loops, check for each i if there is j where i != j and values are same

# Sol'n: Hashing, traverse array twice
from collections import defaultdict
def firstNonRepeat(arr):
    cMap = defaultdict(lambda:0)

    for i in range(len(arr)):
        cMap[arr[i]] += 1
    for i in range(len(arr)):
        if cMap[arr[i]] == 1:
            return arr[i]

    return -1

print('firstNonRepeat:', firstNonRepeat([9, 4, 9, 6, 7, 4]))
        

# Merge two sorted arrays

# Sol'n: track 2 pointers for next element in consideration in each arr, compare and merge
#        O(n1+n2) time and space
def mergeArrays(arr1, arr2):
    # Kind of like merge part of merge sort
    arr3 = [None] * (len(arr1)+len(arr2))
    # Simultaneously traver arr1 and arrr2
    i = j = k = 0
    while i < len(arr1) and j < len(arr2):
        # Add min of 2 to arr3, move ahead in arr3 and in array of el who was picked
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i += 1
        else:
            arr3[k] = arr2[j]
            j += 1
        k += 1
    # check for remaining elements
    while i < len(arr1):
        arr3[k] = arr1[i]
        i += 1
        k += 1
    while j < len(arr2):
        arr3[k] = arr2[j]
        j += 1
        k += 1
    
    return arr3

arr1 = [3,8,12]
arr2 = [2,6,11]
print('mergeArrays:', mergeArrays(arr1, arr2))


# Additional... Merging 2 sorted arrays with O(1) extra space???
#   Idea: Is to begin from the last element of arr2 and search it in arr1, if there is a greater element in arr1, 
#         move all elements one position ahead and move last el of arr1 to arr2
#   To Keep arr1 and arr2 sorted, can use insertion sort type of insertion for this by finding the smallest element in arr1 greater than arr2[i])


# Tradeoff space for time O(m*n) ---> worst case arr1 > arr2
# Iterate from last el of arr2[i], find smallest el in arr1 that's greater than arr2[i] and fit arr2[i] in there
#  Move last el of arr1 to arr2[i]

# Effectively an INSERTION SORT TYPE insert arr2 into arr1
def mergeArraysOpt(arr1, arr2, m, n):
    for i in range(n-1, -1, -1):
        # find smallest el in arr1 > arr2[i]
        last = arr1[m-1]
        j = m-2 # avoid j-1 index out of bounds
        while j >= 0 and arr1[j] > arr2[i]: 
            # move all el 1 pos ahead until smallest greatest found
            arr1[j+1] = arr1[j]
            j -= 1
        # check if there is greater el, edge case check last
        if j < m-2 or last > arr2[i]:
            arr1[j+1] = arr2[i]
            arr2[i] = last
    


arr1 = [3,8,12]
arr2 = [2,6,11]
print('mergeArraysOpt:')
mergeArraysOpt(arr1, arr2, len(arr1), len(arr2))
print(arr1, arr2)


# Note [ALTERNATING] 2 step!
# Rearrange positive and negative numbers in O(n) and O(1) extra space

# O(n) space pretty easy, create 2 sub-arrays for pos and neg
# O(1) space separate pos and neg using partition process of quicksort, consider 0 as pivot
#      start with first neg & first pos, swap every alternative neg with pos
# NOTE: the order of the appearance of elements is not maintained with this approach

def rearrange(arr):
    # similar to partition process of quicksort
    i = -1 # point right before the pivot point
    for k in range(len(arr)):
        if arr[k] < 0:
            # update i to new pivot point and swap
            i += 1
            arr[i], arr[k] = arr[k], arr[i]
    
    # now neg at start, pos at end, init starting indices
    neg, pos = 0, i+1

    # Slow fast ptr approach to swap alternatively
    # inc neg by 2 and pos by 1 - swap every other neg with pos
    while pos < len(arr) and neg < pos and arr[neg] < 0:
        # swap
        arr[pos], arr[neg] = arr[neg], arr[pos]
        neg += 2
        pos += 1
    return arr
    
print('rearrange:', rearrange([-1,-2,-3,-4,5,-10,6,8]))









