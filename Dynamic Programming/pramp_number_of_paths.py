# Like leetcode unique paths but restriction that car can't cross diagonal border

def num_of_paths_to_dest(n):


  # recursive approach
  # return num_paths(0,0,n)
  
  # [MEMOIZATION] is top-down
  # Bottom up would be Tabulation
  
  # init to -1 to indicate uncomputed
  memo = [[-1]*n for _ in range(n)]
  def num_paths(x,y):
    # consider special cases
    # invalid x or y
    if x < 0 or y < 0:
      return 0
    # crossed the border to upper half
    if x < y:
      memo[x][y] = 0 # invalid path
    elif x == 0 and y == 0:
      memo[x][y] = 1
    elif memo[x][y] != -1:
      return memo[x][y]
    else:
      memo[x][y] = num_paths(x-1,y) + num_paths(x,y-1)
    return memo[x][y]
  
  return num_paths(n-1,n-1)
    
      

# destination always (n-1,n-1)

'''
Bottom up not as intuitive as top down approach...
at every point, car can either go 1 up or 1 right 
'''

# Hmm - generally top down recursion is more intuitive 
#       paths(i,j) = paths(i-1,j) + path(i,j-1)
def num_paths(x, y, n):
  if x == n-1 and y == n-1:
    print('found base case')
    return 1
  # catch case where x,y is on the border
  # cannot cross but can still touch the border
  if x != 0 and x > y or (x >= n or y >= n):
    print('border passed',x,y)
    return 0
  # sum the paths 
  print(x,y)
  # WRONG - We should be building sol'n from sol'n of subproblems
  # Start from x=n-1,y=n-1
  return num_paths(x,y+1,n) + num_paths(x+1,y,n)

print('huuh')
print(num_of_paths_to_dest(4))
  
# Can this be memoized?
# dp[x][y] are num paths to get from x,y to n-1,n-1


  
  
# Pseudo for Tabulation on lower half of the grid

function numOfPathsToDest(n):
    if (n == 1):
        return 1

    lastRow = []
    for i from 1 to n-1:
        lastRow[i] = 1 # base case - the first row is all ones

    currentRow = []
  
    # IMPORTANT NOTE: We're only calculating every square south-east to the diagonal
    for j from 1 to n-1:
        for i from j to n-1:
            if (i == j):
                # this makes sense if you draw out the grid, then currentRow[i] on the border and 
                # same number of paths as lastRow[i]
                currentRow[i] = lastRow[i]
            else:
                currentRow[i] = currentRow[i-1] + lastRow[i]
        lastRow = currentRow

    return currentRow[n-1]
