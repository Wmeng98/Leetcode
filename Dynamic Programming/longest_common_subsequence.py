# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
# LCS: Given two sequences, find the length of longest subsequence present in both of them

# subsequence: A sequence that appears in the same relative order, but not necessarily contiguous

# String with length n has 2^n - 1 different subsequences. We don't consider the the subs with length 0

# [BRUTE FORCE] 
# Time complexity is O(m*2^n) 
# Where m is length of string T and n is length of string S. We check all subsequences of S if it's also in T


# [NAIVE RECURSIVE IMPLEMENTATION]

# Recursive definition of L(X[0..m-1], Y[0..n-1])
# 
# If the last characters of both sequences match (X[0..m-1] == Y[0..n-1]) then...
#      L(X[0..m-1], Y[0..n-1]) = 1 + L(X[0..m-2], Y[0..n-2])
# If the last characters of both sequences do not match (X[0..m-1] != Y[0..n-1]) then...
#      L(X[0..m-1], Y[0..n-1]) = MAX(L(X[0..m-2], Y[0..n-1]), L(X[0..m-1], Y[0..n-2]))

def lcs(X, Y, m, n):
    # check base case
    if m == 0 or n == 0:
        return 0
    # check if last char of both seq match
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m-1, n), lcs(X, Y, m, n-1))

x = "ABCDGH"
y = "AEDFHR"
print(lcs(x, y, len(x), len(y)))

# Time O(2^n) when all characters of X and Y mismatch


# [TABULATED IMPL FOR LCS PROBLEM]

def lcs_dp(X, Y):

    m = len(X)
    n = len(Y)

    # declare arr to to store dp vals
    L = [[None]*(n+1) for i in range(m+1)]

    # Build L[m+1][n+1] in bottom up fashion
    # L[m][n] contains length of lcs for first m char of X and first n char of Y
    for i in  range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = 1 + L[i-1][j-1]
            else:
                L[i][j] = max(L[i][j-1], L[i-1][j])
    
    return L[m][n]

x = "ABCDGH"
y = "AEDFHR"
print(lcs_dp(x, y))

# Time O(mn)

# TODO: Space optimized LCS and print LCS