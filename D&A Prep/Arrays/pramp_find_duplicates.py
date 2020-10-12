# Time: O(N+M)
# Space: O(min(N,M))
def find_duplicates_non_optimized(arr1, arr2):
  p1 = set(arr1) # O(N)
   
  output = [] # O(Min(M,N))
  for p in arr2:
    if p in p1:
      output.append(p)
  
  # output
  return output


def binary_search(arr, val):
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
  
 
def find_duplicates(arr1, arr2):
  if len(arr1) < len(arr2):
    small = arr1
    big = arr2
  else:
    small = arr2
    big = arr1
  
  output = []
  for passport in arr1:
    if binary_search(arr2, passport) != -1:
      output.append(passport)
  
  return output
  
# NlogM
# a1 = [5,6] N
# a2 = [0...100] M

arr1 = [1, 2, 3, 5, 6, 7] # N
arr2 = [3, 6, 7, 8, 20] # M

print(find_duplicates(arr1, arr2))
print(pow(2, 32))
print(8 * 32)