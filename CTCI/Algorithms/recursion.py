'''

Recursion

* "Design an algorithm to compute the nth"
* "Write code to list the first n..."
* "Implement a method to compute all..."

How To Approach
    * recursive solutions built off of solutions to subproblems
    1. to compute f(n), add/remove/changing the solution to f(n-1)
    2. solve problem for first half of dataset, then second half, and then merge

    3 ways to divide problem into subproblems
        1. Bottom-up
        2. Top-down 
        3. Half-and-half
    
Bottom-up
    Solve soln for smaller subproblem and build from there, 1 el, 2 el, 3 el, etc.
Top-down
    Solving problem in a more "natrual manner"
    Think about how we can divide the problem for case N in to subproblems
    Be careful of overlap between cases
Half-and-half
    Often effective to divide dataset in half
    Binary search, Merge sort

All recursive algorithms can be implemented iteratively (complexity varies)

[Solving Recurrences]
    3 ways to solve
        1. Subsitution: 
            take a guess, use induction to prove it's right
        2. Recurrence tree: 
            draw recurrence tree and calculate time taken by every level of the tree, sum work done at all levels
        3. Master method: 
            works only for a certain type of recurrences that can be transformed to following type... (NOTE: mainly derived from recurrence tree method)

'''

'''

[Recurrence Tree]

1. Draw recurrence tree
2. get height of recursion tree (subproblem size == 1???)
3. cost of each level of tree (NOTE: base case is last level, T(1) operation on all nodes)
4. sum cost of each level

NOTE: cost of last level can be deduced to n^(log_b(a)) ---> MASTER THEOREM !!!
    Reason to deduce to base n is easier to compare with cost of internal levels

NOTE:
    Special case: 𝑇(𝑛)=𝑇(𝑛3)+𝑇(2𝑛3)+𝑛 

        Key here is sum of work each level adds up to n --> O(nlogn) NOTE: Finding TIGHT upper and lower bound

        If it was 𝑇(𝑛)= 2𝑇(2𝑛3)+𝑛 ---> work exponentially increases as we get deeper, master thm O(n^2)


'''

'''

[Master Theorem] - used in calculating the complexity of recurrence relations

T(n) = aT(n/b) + f(n),

where,
n = size of input
a = number of subproblems in the recursion
n/b = size of each subproblem. All subproblems are assumed 
     to have the same size.
f(n) = cost of the work done outside the recursive call, 
      which includes the cost of dividing the problem and
      cost of merging the solutions

Here, a ≥ 1 and b > 1 are constants, and f(n) is an asymptotically POSITIVE function (NOTE: always increasing).

NOTE: There are following three cases:

1. If f(n) = Θ(n^c) where c < Logba then T(n) = Θ(n^(Logba)) ---> leaves are dominant, work done on leaves polynomially more
2. If f(n) = Θ(n^c) where c = Logba then T(n) = Θ(n^c*Log n) ---> work done on leaves/root asymptotically same
3.If f(n) = Θ(nc) where c > Logba then T(n) = Θ(f(n)) ---> work done by root is asymptotically more




Inadmissable Relations
    * a is not a constant (i.e 2^n)
    * a < 1 (i.e 0.5)
    * f(n) is not asymtotically positive


NOTE:, NLOGN only when same amount of work done on each level
    i.e T(n) = 16T(n/4) + n ----> (Case 1)

'''