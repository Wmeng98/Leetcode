'''

Heap data structure available using "heapq" module

NOTE: Used for min-heap only
    There are undocumented functinos for max heap like 
        heapq._heapify_max(iterable)
        NOTE: push/pop methods break the max heap data structure

Solutions for using max-heaps
    1. negate your values when you store them in heap
    2. More practical (without changing the data) solution is to invert object comparison, need to define new wrapper obj


'''

import heapq as hq


class MaxHeapObj(object):
  def __init__(self, val): self.val = val
  def __lt__(self, other): return self.val > other.val # INVERSION HERE
  def __eq__(self, other): return self.val == other.val
  def __str__(self): return str(self.val)

maxh = []
hq.heappush(maxh, MaxHeapObj(x))
x = maxh[0].val  # fetch max value
x = hq.heappop(maxh).val  # pop max values

# If need differentiate between the two, add classes for max/min heap objects (MaxHeap, MinHeap)

'''

Various operations on Heap

* heapify(iterable) - convert iterable into heap order
* heappush(heap, ele) - insert element into heap, heap order maintained
* heappop(heap) - remove and return smallest element from the heap, heap order maintained
* 
* heappushpop(heap, ele) - combines function of both push & pop operations in one statement, increases efficiency
* headreplace(heap, ele) - element is FIRST popped, then the element is pushed i.e, smallest value originally in the heap is popped

* nlargest(k, iterable, key = fun)
* nsmallest(k, iterable, key = fun)
    NOTE: IMPLEMENTATION: Space optimized O(t) for t largest/smallest
    
    Heapify only first t el of iterable O(t), then remaining el added to heap via heappushpop one at a time O(logt)
    O(n*logt) + O(tlogt) [heap is sorted at the end]

'''

# NOTE: Heapify will work with lists of tuples such that the first element of each tuple is the value, so use (distance, node) instead
# NOTE: Or you can add lt (python3) / cmp (python2) operator to custom class


class HeapObj(object):
  def __init__(self, val): self.val = val
  def __lt__(self, other): return self.val < other.val

h = []
hq.heappush(h, HeapObj(10))

'''
NOTE: Heaps break tie on tuples by using next el in tuple
      To avoid, use custom object with __lt__ override
'''