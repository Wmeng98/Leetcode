'''

Merge Sort, Quick Sort, Bucket Sort
  Most commonly used in interviews

Stability in sorting algorithms
	A sorting algorithm is said to be stable if two objects with equal keys appear in the same order in sorted output as they appear in the input array to be sorted.

'''

################################################################################################################################################################
'''
Bubble Sort

Simplest, works by repeatedly swapping adjacent el if they are in wrong order
Need one whole pass without swap to indicate done sorting

NOTE: After 1 whole pass of the arr, the last el will be in proper place
NOTE: After ith pass, last i elements will be sorted in proper place

[RUNTIME] O(n^2) worst case, O(n) best case (sorted already) 
[SPACE] O(1) auxillary

STABLE!!!
'''

def bubbleSort(arr, n):
	for i in range(n):
		# last i el will be sorted
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1]:
				# swap, don't even need a temp in python
				arr[j], arr[j+1] = arr[j+1], arr[j]

				
# Above always runs O(n^2) even if the array is already sorted
# Optimize by stopping the algo is no swaps made in inner loop

def bubbleSort2(arr, n):
	for i in range(n):
		swapped = False
		# last i el are sorted
		for j in range(0, n-i-1):
			if a[j] > a[j+1]:
				swapped = True
				a[j], a[j+1] = a[j+1], a[j]
		# break if no 2 el were swapped by inner loop
		if not swapped:
			break

# Can be done RECURSIVELY too!
#   Each pass, fix last el of current subarray
	
# tests
arr1 = [2,4,3,1,9]
bubbleSort(arr1, len(arr1))
print('bubbleSort', arr1)

################################################################################################################################################################

'''
Selection Sort

Repeatedly finding minimum (select) from unsorted and put into sorted (subarray if in place)

NOTE: Never makes more than O(n) swaps, useful when memory write is costly

[RUNTIME] 2 nested loops O(n^2)
[SPACE] O(1) auxillary 

NOT STABLE - step of swapping a pair of element could possibly change relative order of another pair of elements that have equal keys
	2 2' 1
	1 2' 2

'''

def selectionSort(arr, n):
	for i in range(n):
		# find min in unsorted subarray i..n-1 and swap it with i
		minId = i
		for j in range(i+1, n):
			if arr[minId] > arr[j]:
				minId = j
		# swap min found with first
		arr[i], arr[minId] = arr[minId], arr[i]
	
# tests
arr1 = [2,4,3,1,9]
selectionSort(arr1, len(arr1))
print('selectionSort', arr1)



################################################################################################################################################################

'''
Insertion Sort

Values picked from unsorted and put into correct position in the sorted array

NOTE: 

[RUNTIME] 2 nested loops O(n^2) -> worst case
[SPACE] O(1) auxillary 

STABLE

Binary Insertion Sort - reduce search time, but swaps still make it O(n^2) time

Insertion Sort in Singly Linked List
	Can seach starting from front bc don't need to worry about shifting!!!
	Can make it stable
'''
# Note move el one pos up to make space for insertion
def insertionSort(arr, n):
	for i in range(1, n):
		key = arr[i]
		# Move el of arr[0...i-1] that are greater than key to 1 pos ahead of their curr
		j = i-1
		# More convenient to start from back of sorted subarray to shift and search as we go
		while j >= 0 and key < arr[j]:
			arr[j], arr[j+1] = arr[j+1], arr[j]
			j -= 1
		arr[j+1] = key
	
# tests
arr1 = [2,4,3,1,9]
insertionSort(arr1, len(arr1))
print('insertionSort', arr1)

################################################################################################################################################################

'''
QuickSort

Divide and Conquer algo like MergeSort
Pivot and Partition

KEY PROCESS in quicksort is the partition method
	partition takes linear time and puts x at correct pos in arr


[RUNTIME] Generally T(n) = T(k) + T(n-k-1) + \theta(n) 
	k = # el smaller than pivot

	Worst case: partition picks greatest or smallest el as pivot
		T(n) = T(0) + T(n-1) + \theta(n) ---> \theta(n^2)
	Best case: parition picks middle el as pivot
		T(n) = 2T(n/2) + \theta(n) ---> \theta(nlogn)
	Average case: 
		Consider all permutations and calc time taken for each
		tl;dr O(nlogn)

NOTE: QuickSort can be implemented in different ways by changing the choice of pivot, so that the worst case rarely occurs for a given type of data.

[SPACE] in-place, memory for stack though worst case is O(n)

UNSTABLE - but can make stable

ADDITIONAL OPTIMIZATIONS...

A three partition Quick Sort would pick two values to partition on and split the array up that way
3, 2, 0, 2, | 4, 6, 5, 7, | 8, 8, 9

NOTE: IDEA is BASED Tail recursion optimization (not actually Tail recursion, just reduce # recursive calls)
	Optimize the above code to make a recursive call only for the smaller part after partition, larger handled in WHILE loop

NOTE: Tail recursion argument: Since the recursive call is the last statement, there is nothing left to do in the current function, so saving the current function’s stack frame is of no use

TODO: QuickSort vs. MergeSort

'''

'''
Pseudo...

# low - low index, high - ENDING INDEX
quickSort(arr[], low, high):
	if low < high:
		pi = partition(arr, low, high) # pi - pivot, arr[pi] now in right place

		quickSort(arr[], low, pi - 1) // before pivot
		quickSort(arr[], pi + 1, high) // after pivot


partition(arr, low, high):
	# choose rightmost as pivot
	# KEY: start at leftmost, track index of <= el as i, if find smaller, SWAP curr with arr[i], o/w ignore

	# pivot el to be placed at right pos
	pivot = arr[high]

	i = low - 1
	for j in range(low, high):
		if arr[j] <= pivot:
			i++
			# swap to left of pivot
			swap arr[i], arr[j]
	# swap pivot to i pos
	swap arr[high], arr[i+1]
	return i+1

'''

def quickSort(arr, low, high):
	if low < high:
		# partition st. pivot in right place
		pi = partition(arr, low, high)

		quickSort(arr, low, pi - 1)
		quickSort(arr, pi + 1, high)

def partition(arr, low, high):
	# pick high as the pivot
	pivot = arr[high]
	i = low - 1 # i tracks current pivot point
	for j in range(low, high):
		# move all el <= pivot to the left of index i
		if arr[j] <= pivot:
			# update new pivot and swap curr with arr[i]
			i += 1
			arr[j], arr[i] = arr[i], arr[j]
	# move pivot to proper location
	arr[high], arr[i+1] = arr[i+1], arr[high]
	return i+1

### BONUS QuickSort Iteratively!
'''
Optimize
	1. Choose a better pivot, middle, median of 1st, middle, last
	2. Iteratively, using stacks to store subarray's start/end index for later processing
'''


###

# tests
arr1 = [2,4,3,1,9]
quickSort(arr1, 0, len(arr1) - 1)
print('quickSort', arr1)

################################################################################################################################################################

'''
MergeSort

Like QuickSort, MergeSort is divide & conquer algorithm
merge() function is used for merging 2 halves

[RUNTIME] (n) = 2T(n/2) + θ(n) ---> O(nlogn) ---> worst, average, best ---> ALWAYS DIVIDES ARR INTO 2 HALVES
[SPACE COMPLEXITY]
	MergeSort is a recursive algorithm, therefore space complexity is O(logN) for both array & LL use cases
	Will also create temp arrays in recursive calls, won't co-exist, O(n + logn (stack space)) ---> n (# el in array) dominates 
	
	O(n)

STABLE

NOTE: MergeSort linkedlists in O(nlogn) time
	merge operation can be impl without extra space.
	Optimize [space complexity] to O(logn)

NOTE: 3 Way MergeSort 
	[RUNTIME] O(nlog_3(n)).. 
	Although time complexity looks less compared to 2 way merge sort, the time taken actually may become higher because number of comparisons in merge function go higher.

NOTE: MergeSort vs. QuickSort
	Partition on el in array
	Worst case complexity
	datasets - quicksort worse with large dataset with many repeated els (creates n^2 QUADRATIC runtime)
		Quicksort works faster in smaller datasets
	stability
	Locality of reference
		quicksort - good cache locality?

		quicksort changes the array inplace - in the array it is working on [unlike merge sort, for instance - which creates a different array for it]. 
		Thus, it applies the principle of locality of reference.

		Cache benefits from multiple accesses to the same place in the memory, since only the first access needs to be actually taken from the memory - 
		the rest of the accesses are taken from cache, which is much faster the access to memory
'''

'''
PseudoCode

mergesort(arr, l, r)
	// find mid point to divide array into 2 halves
	mid = len(arr)//2
	// call mergesort on first half
	mergesort(arr, l, m)
	// call mergesort on second half
	mergesort(arr, m+1, l)
	// merge the two halves together
	merge(arr, l, m, r)

'''
# PASSING SUBARRAYS
def mergesort_1(arr):
	if len(arr) > 1:
		# Find middle of array
		mid = len(arr)//2
		# divide arr into 2 subarrays
		L = arr[:mid]
		R = arr[mid:]
		# run mergesort on each
		mergesort_1(L)
		mergesort_1(R)
		# Finally merge the 2 sorted subarrays together
		merge_1(arr, L, R)

def merge_1(arr, L, R):
	i = j = k = 0
	while i < len(L) and j < len(R):
		if L[i] < R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[i]
			j += 1
		k += 1
	# check for remaining unmerged el and add them
	while i < len(L):
		arr[k] = L[i]
		i += 1
	while j < len(R):
		arr[k] = R[j]
		j += 1

# PASSING INDICES
def mergesort_2(arr, l_index, r_index):
	# base case
	if l_index >= r_index:
		return
	# get middle index (l + r)/2
	mid_index = (l_index + r_index)//2
	# run mergesort on subarrays
	mergesort_2(arr, l_index, mid_index)
	mergesort_2(arr, mid_index+1, r_index)
	# merge sorted subarrays
	merge_2(arr, l_index, r_index, mid_index)


def merge_2(arr, l, h, m):
	# make copies of subarrays we trying to merge
	# TRICKY; second param non-inclusive, need +1
	L = arr[l:m+1]
	R = arr[m+1:h+1]

	i = j = 0
	k = l # not like v1 where arr is subarray, v2 arr is the whole array!!!
	while i < len(L) and j < len(R):
		if L[i] < R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1	
		k += 1
	# add remaining unmerged el
	while i < len(L):
		arr[k] = L[i]
		i += 1
		k += 1
	while j < len(R):
		arr[k] = R[j]
		j += 1
		k += 1
		
# tests
arr1 = [2,4,3,1,9]
mergesort_1(arr1)
print('mergesort_1', arr1)
arr1 = [2,4,3,1,9]
mergesort_2(arr1, 0, len(arr1)-1)
print('mergesort_2', arr1)

################################################################################################################################################################

'''
BucketSort

Sort el by first dividing several elements into groups called buckets
El inside each bucket sorted using any suitable sorting algorithm

bucketSort()
  1. create N buckets each of which can hold a range of values
  2. for all the buckets
    initialize each bucket with 0 values
  3. for all the buckets
    put elements into buckets matching the range
  4. for all the buckets 
    sort elements in each bucket
  5. gather elements from each bucket
end bucketSort

NOTE: Getting optimal size of each bucket
	(largest_element)\(length_of_list)


[RUNTIME]
	[WORST] O(n^2) -> all in one bucket

	[BEST] O(n+k) -> don't know if k > n
		uniform distributed, already sorted, 

	[AVERAGE] O(n) if each bucket has O(1) items, insertion sort becomes O(1)

[SPACE] O(n+k) -> n number of el in array to be sorted, k is the number of buckets ~ O(n) if k ~ n

'''

def bucketSort(list):
	# find optimal size per bucket
	size = max(list)/len(list)

	# n empty buckets - n = len(list)
	buckets = []
	for i in range(len(list)):
		buckets.append([])
	
	# move el into diff buckets based of range
	for i in range(len(list)):
		j = int(list[i]/size)
		if j < len(list):
			# optimize by using linked list
			buckets[j].append(list[i])
		else:
			buckets[j-1].append(list[i]) # only happens when max
	
	#  sort el within each bucket using insertion sort
	for j in range(len(buckets)):
		insertionSort(buckets[j], len(buckets[j]))
	
	#  concat sorted buckets into one
	# 1 + 2 + 3 + 4 + 5 + 6 + ... n => n^2 NO!
	res = []
	for j in range(len(buckets)):
		# append is O(1) amortized
		for k in range(len(buckets[j])):
			res.append(buckets[j][k])
	
	return res

array = [.42, .32, .33, .52, .37, .47, .51]
print("bucket sort array")
print(bucketSort(array))

################################################################################################################################################################

'''
HeapSort - Heaps

	Comparison based sorting technique based on Binary heap data structure
	Complete binary tree can be easily represented as ann array

	Algorithm
		1. Build heap from input data
		2. Remove root (largest or smallest)
		3. Repeat step 2. while size heap > 1

		NOTE: Heapify procedure can be applied to a node only if its children nodes are heapified. 
			So the heapification must be performed in the bottom-up order.

To build a max-heap from any tree, we can thus start heapifying each sub-tree from the bottom up and end up 
with a max-heap after the function is applied to all the elements including the root element

NOTE: After each heapify call, heap maintains complete binary tree property

* remove root (swap with last, etc.)
	heapify
		REPEAT...

siftUp vs. siftDown for heapify
	building a heap with repeated calls of siftDown has a complexity of O(n) whereas building it with repeated calls of siftUp has a complexity of O(nlogn)
	https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/

	siftDown
		Time taken by each call decreases with the depth of the node because these nodes are closer to the leaves
	siftUp
		Number of swaps increases with the depth of the node because if you are at full depth, 
		you may have to swap all the way to the root. 
		NOTE: As the number of nodes grows exponentially with the depth of the tree, using siftUp gives a more expensive algorithm;
[RUNTIME]
	building max heap is O(n) and heapify is O(logn)
	O(nlogn)
[SPACE]
	In-place
	O(1)

Typical implementation is NOT STABLE but can be made stable

'''

# basically siftdown
def heapify(arr, n, i):
	# init largest as root
	largest = i
	left_child = (2*i)+1
	right_child = (2*i)+2

	# set largest to larger of the 2 children IF THEY EXIST
	if left_child < n and arr[largest] < arr[left_child]:
		largest = left_child
	if right_child < n and arr[largest] < arr[right_child]:
		largest = right_child
	
	# Swap root
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		# continue heapify root
		i = largest
		heapify(arr, n, i)


def heapSort(arr):
	n = len(arr)
	# build max heap, heapify all INTERNAL NODES only
	for i in range(n//2-1, -1, -1):
		heapify(arr, n, i)

	# extract el one by one, IN-PLACE!!!
	for j in range(n-1, 0, -1):
		arr[0], arr[j] = arr[j], arr[0]
		heapify(arr, j, 0) # NOTE: extract largest to end of arr, reduce new size to sort by 1

# Driver code
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print('heapsort', arr)




################################################################################################################################################################

################################################################################################################################################################

################################################################################################################################################################

