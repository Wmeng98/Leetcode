'''

Dynamic Programming

Overlapping Subproblems and Optimal Substructure
    * Shortest Path problem has following optimal substructure property
    * Longest Path problem doesn’t have the Optimal Substructure property
        For example, the longest path q→r→t is not a combination of longest path from q to r and longest path from r to t, because the 
        longest path from q to r is q→s→t→r and the longest path from r to t is r→q→s→t

Take recursive algorithm, finding overlapping subproblems, and caching those results for future recrusive calls (memoization)
Alternatively, study pattern of recursive call and implement iteratively (bottom-up)

Steps to solve DP
    1. Recognize it's DP
        Ask whether problem soln can be expressed as a func of solns to similar smaller problems

    2. Identify problem variables
        parameters that change every subproblem
        Ex. array pos, speed
    
    3. Recurrence relation
        how to compute main problem with the subproblems?

    4. Base cases
        subproblem that doesn't depend on any other subproblem
        Look for constraints of the problem
    
    5. Iterative or Recursive?
        Stack overflow issues typcically deal breaker to avoid recursion
    
    6. Add Memoization
    
    7. Determine Time Complexity


'''

# Fibonacci Numbers

def fibonacci(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    return fibonacci(i-1) + fibonacci(i-2)

# Memoization: compute and cache result for future use

def fib(i):
    return fibMemoized(i, [0]*(i+1))

def fibMemoized(i, memo):
    if i == 0 or i == 1:
        return i
    if memo == 0:
        memo[i] = fibMemoized(i-1, memo) + fibMemoized(i-1, memo)
    
    return memo[i]

'''

Bottom-Up Dynamic Programming

Iterative approach, no recursion

'''

# NOTE: Can be space optimized, only use memo for i-1 and i-2, 2 variables to store

def fibBottomUp(i):
    if i == 0 or i == 1:
        return i
    memo = [0]*(i+1)
    memo[1] = 1

    for j in range(2, i+1):
        memo[j] = memo[j-1] + memo[j-2]
    
    return memo[i]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

'''

[Minimize number of operations required to obtain N]

Given an integer N, the task is to obtain N, starting from 1 using minimum number of operations. The operations that can be performed in one step are as follows

Approach
    *  dp[i] = Minimum number of operations to obtain i from 1 
    *  dp[x] = min(dp[x-1], dp[x/2], dp[x/3])

[TIME] O(n)
[SPACE] O(n)

'''
########################################

'''

[Longest Increasing Subsequence]

The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order.

Approach
    a[0...n-1] be input array
    L(i) length of the LIS ending at index i s.t arr[i] is last el of LIS

    L(i) = 1 + max( L(j) ) where 0 < j < i and arr[j] < arr[i]; or
    L(i) = 1, if no such j exists.

'''

# Recursive approach [TIME] Exponential

'''
    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2]
       IF arr[n-1] is smaller than arr[n-1], and max ending with
       arr[n-1] needs to be updated, then update it"""

    for i in xrange(1, n):
        res = _lis(arr , i)
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
            maxEndingHere = res +1
'''

# Iterative (memoized bottom-up)
# [TIME] O(n^2)
# [SPACE] O(n)

def LIS(arr, n):
    # init LIS values for all indexes
    lis = [1]*n
    # compute optimized lis in bottom-up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    
    maximum = 0
    # pick max of all LIS values
    maximum = max(lis)

# Driver program to test above function
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print "Length of lis is", lis(arr)

########################################
'''

[Maximum Length Chain of Pairs]

You are given n pairs of numbers. In every pair, the first number is always smaller than the second number. A pair (c, d) can follow another pair (a, b) if b < c. 
Chain of pairs can be formed in this fashion. Find the longest chain which can be formed from a given set of pairs. 

NOTE: Variation of the longeest incrementing subsequence

Approach
    Sort in increasing order of first/smaller element
    Run modified LIS to compare 2nd el of finalized LIS with first el of new LIS being constructed


'''

# Bottom-up
# [TIME] O(n^2)

from operator import itemgetter

class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

def maxChainLength(arr, n):
    # NOTE: Assume arr already sorted

    max = 0
    # init MCL for all indices
    mcl = [1]*n
    # compute optimized chain length bottom-up
    for i in range(1, n):
        for j in range(0, i):
            if arr[j].b < arr[i].a and mcl[i] < mcl[j] + 1:
                mcl[i] = mcl[j] + 1
    
    # mcl now stores max chain length ending with pair i
    return max(mcl, key=itemgetter(1))

# Driver program to test above function
arr = [Pair(5, 24), Pair(15, 25),
       Pair(27, 40), Pair(50, 60)]
 
print('Length of maximum size chain is',
      maxChainLength(arr, len(arr)))


# Top-down recursive memoized
'''
first step is to figure out the recurrence relation. 
NOTE: The best and the easiest way to get the recurrence relation is to think about the choices that we have at each state or position

Choice 1: To select the element at the particular position and explore the rest, (or) 
Choice 2: To leave the element at that position and explore the rest. 

    T(n) = max( maxlenchain(p,n,p[pos].second,0)+1,maxlenchain(p,n,prev_choosen_ele,pos+1) ) 
    * NOTE: 0 pos here bc assume p[] is NOT sorted, o/w would be pos+1

'''

########################################

'''

[Find min number of coins that will make a given value]

Given a value V, if we want to make change for V cents, and we have infinite supply of each of C = { C1, C2, .. , Cm} valued coins, 
    what is the minimum number of coins to make the change? If it’s not possible to make change, print -1

This problem is a variation of the problem discussed Coin Change Problem. Here instead of finding total number of possible solutions, 
    we need to find the solution with minimum number of coins



If V == 0, then 0 coins required.
If V > 0
   minCoins(coins[0..m-1], V) = min {1 + minCoins(V-coin[i])} 
                               where i varies from 0 to m-1 
                               and coin[i] <= V

'''

# Recursive [TIME] exponential
def minCoins(coins, m, V):
    # base case
    if V == 0:
        return 0
    
    # init result
    res = float('inf')

    # Try every coin with a smaller value than V
    for coin in coins:
        if coin <= V:
            subRes = minCoins(coins, m, V-coin)
            # check if res can be minimized
            if subRes != float('inf') and res > subRes + 1:
                res = subRes + 1
    
    return res


# Iterative Bottom-up
# [TIME] O(mV)
# [SPACE] O(V)

def minCoinsMemo(coins, m, V):
    # table[i] store min coins for value i
    table = [0]*(V+1)
    # base case, V == 0
    table[0] = 0

    # init all table values as inf
    for i in range(1, V+1):
        table[i] = float('inf')
    
    # compute min coin for all V from 1 to V
    for i in range(1, V+1):
        # for coins smaller than i
        for coin in coins:
            if coin <= i:
                if table[i-coin] != float('inf') and table[i] > table[i-coin] + 1:
                    table[i] = table[i-coin] + 1
    
    if table[V] == float('inf'):
        return -1
    return table[V]

# Driver Code
coins = [9, 6, 5, 1]
m = len(coins)
V = 11
print("Minimum coins required is ",
                minCoins(coins, m, V))




########################################
########################################
########################################
########################################