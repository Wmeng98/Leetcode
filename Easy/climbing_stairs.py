# Solution 1 - Brute force
#  - recursive approach (all possible step combinations)
#  - O(2^n) and O(n) space

# Solution 2 - Memoization
#  - prune recursion tree with the help of memo array
#  - redundantly calculating the result for every step
#  - O(n) time and space

# Solution 3 - DP
#  - optimal sol'n can be constructed from optimall sol'n of subproblem
#  - dp[i] denote number of ways to reach the ith step

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n==1:
        return 1
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]
 
# Solution 4 - Optimized Space O(1)
#  - Note that dp[i] is asking for ith fibonnaci number
