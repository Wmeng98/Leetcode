# Similar to Pramp - Number of Paths Question

'''

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Time: exponential

'''
# Note: In this example, initial state of the car is (m,n) -> try to get to (1,1) not (0,0)
#       Whereas in Pramp, it was (0,0)

# Recursive Approach
def unqiuePaths(m,n):
    # can either move down (n-1) or right (m-1)

    # KEY: we can check as long as m is bottom row or n is last col - only 1 path to dest

    if m == 1 or n == 1:
        return 1
    # base case
    else:
        return unqiuePaths(m-1,n) + unqiuePaths(m,n-1)

print('recursive unqiuePaths:', unqiuePaths(3,7))


'''

Above recursive sol'n not enough to pass all the test cases within timeout

Could use tabulation (simple in this case)
dp[m][n] = num paths to m,n cell

Can INIT array with dp[m][1...n] = dp[1...m][n] = 1 because we start at m,n

Time: O(m*n)
Space: O(m*n)

NOTE: Because we use 2D dp to memoize - indexing starts at 0
Therefore answer will be at dp[m-1][n-1]

Building dp from 0,0 to m-1,n-1 where dp[m][n] represents the number of
paths to get from 0,0 to m-1,n-1

'''

# DP Approach
def dpUnqiuePaths(m,n):
    dp = [[1]*n for row in range(m)]

    # start with col as outer
    for col in range(1,n):
        for row in range(1, m):
            # can either move down (n-1) or right (m-1)
            dp[row][col] = dp[row-1][col] + dp[row][col-1]
    return dp[m-1][n-1]

print('iterative dp unqiuePaths:', dpUnqiuePaths(3,7))
