# https://www.geeksforgeeks.org/merge-sort/

# merge(arr,l,m,r) is a key process assuming that arr[l..m] and arr[m+1..r] are sorted and merges the sub-arrays into one

# Recursive implementation

# Space complexity is O(n)+O(logn) counting stack frames -> still O(n) in case of arrays

def mergeSort(arr):
    # base case, need at least 2 el in arr to divide
    if len(arr) > 1:
        mid = len(arr) // 2
        # Divide to L and R sub-arrays
        L = arr[:mid]
        R = arr[mid:]

        # sort the first and seconds halves
        mergeSort(L)
        mergeSort(R)

        # merge the two sub-arrays
        i = j = k = 0
        while i < len(L) and j < len(R):
            # Merge back into arr
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # check for remaining el
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

arr = [12,11,2,4,3,9,5,7,0]
print('before merge sort:', arr)
mergeSort(arr)
print('after merge sort', arr)


