# Solution 1 - Backtracking
#  graph traversal problem
#  determine if the corresponding graph is a DAG (Directed Acyclic Graph)

# Typical strategy for graph traversal problems would be backtracking or simply DFS

# Backtracking
#  General algorithm often applied to solve CSP
#  Incrementallly build candidates to the solutions, and abandons a candidate (backtrack) ASAP when it learns not a valid solution

# General Idea
#  Enumerate each course, to check if it could form a cyclic dependency
#  Breadcrumb our path (mark nodes we visited). Remove for each iteration

# Complexity
#  Worst case is when all the nodes are chained up in a line Sum(i=1, V)i = |V|*|V+1|/2
#  O(E + V^2)

