'''

Binary Search - sorted arrays

[RUNTIME] O(logn)
[SPACE] O(logn) for recursive call stack space and O(1) for iterative

'''

def iterativeBS(arr, val):
    low = 0
    high = len(arr) - 1

    while low <= high:
        # mid = ((high - low + 1) // 2) + low
        mid = (low + high) // 2
        if arr[mid] == val:
            return mid
        if arr[mid] < val:
            # constrain search to right half
            low = mid + 1
        else:
            # constrain search to left half
            high = mid - 1
    return -1

arr = [1,2,3,4,5,6,7,8,9,10]
arr2 = [1,2,3,4,5,6,7,8,9]
print('iterative binary search', iterativeBS(arr, 3))
print('iterative binary search', iterativeBS(arr2, 8))

def recursiveBS(arr, val, low, high):
    if low > high:
        return -1
    mid = (low+high)//2
    if val == arr[mid]:
        return mid
    elif val < arr[mid]:
        # NOTE: already considered mid
        return recursiveBS(arr, val, low, mid-1)
    else:
        return recursiveBS(arr, val, mid+1, high)

arr = [1,2,3,4,5,6,7,8,9,10]
arr2 = [1,2,3,4,5,6,7,8,9]
print('recursive binary search', recursiveBS(arr, 3, 0, len(arr) - 1))
print('recursive binary search', recursiveBS(arr2, 8, 0, len(arr2) - 1))   