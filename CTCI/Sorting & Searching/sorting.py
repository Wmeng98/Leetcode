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
NOTE: After ith pass, last i el will be sorted in proper place

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

################################################################################################################################################################

################################################################################################################################################################

################################################################################################################################################################

################################################################################################################################################################

################################################################################################################################################################

################################################################################################################################################################

################################################################################################################################################################

################################################################################################################################################################