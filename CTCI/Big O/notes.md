# Big O

Asymptotic analysis (describe limiting behavior) for the estimation of computational complexity.

## Big O, Big Theta, and Big Omega

- big O: upper bound on time/space, O(N) -> at **least** as fast as N
- big omega: lower bound on time/space, Ω(N) -> **wont be faster** than N
- big theta: tight bound on runtime/space, θ(N) -> both O(N) and Ω(N)

## Best, Worst, Expected Case

Best, Worst, Expected cases all describe big O (runtime) for particular inputs/scenarios

## Space Complexity

Stack space (levels of the stack) in recursive calls count for space complexity.\
Note calls need to simultaneously exist on the call stack to take up additional space

## Drop the Constants

- contstants
- non-dominant terms

## Amortized Time

Average running time of an operation

## Log N Runtimes

number of elements in problem space are reduced by some proportion (halved, thirds, etc.)

> Note we drop base for logs because any two logarithms differ by constant factor (by **change of base formula**, logs are constant multiples of one another)

>log𝑎𝑛=Θ(log𝑏𝑛) for all 𝑎,𝑏>1

## Recursive Runtimes

Tree depth vs. height vs. levels
- For each node in a tree, we can define two features: **height** and depth. A node's height is the number of edges to its most distant leaf node. On the other hand, a node's **depth** is the number of edges **back up to the root**

**floor[log_2(N)]** where N is number of nodes in a binary tree is getting the height of that tree (height)\
Now the ^ is asymptotic (limiting behavior), # nodes in a perfect binary tree is `2^(k+1)-1 = n (total # nodes)` where  k is the depth. therefore `k = log_2(n+1/2) -> O(logn)`\
Note: consider when subproblem becomes size 1

> **Note: Easier to reason runtime logn as reducing original problem by a certain proportion**

```
Depth can be calculated in 2 ways.

floor(log_2(N)) -> N is number of nodes in the binary tree
ceil(log_2(n)) -> n is number of elements in array (leaf nodes/last level)
```

> Note: Number of el in array directly proportional to number of **leaf nodes (not # nodes on last level)** when creating a BST \
> Note: that each level has one more node that the entire above it


consider f(n-1)+f(n-1)
- with recursive functions making multiple calls, the runtime will often look like O(branches^depth) -> O(2^N).
- Note that runtime is asymptotic as the formula for the actual # nodes of a BINARY TREE is bounded by `2^0 + 2^1 + .. + 2^N` which is `2^(N+1) - 1`
- Note space complexity is `O(N)` as only O(N) nodes exist at any given time

> Note base of a log doesn't matter since bases only differ by constant factor. However, this **doesn't apply to exponent bases**. 8^N -> (2^3)^N -> 2^3N -> 2^2N * 2^N and 2^N are differet by a factor of 2^2N **which is not a constant factor**.

## Examples

Example 3
- inner loop starts at i+1
- First iteration through, j runs for N-1 steps...
- (N-1) + (N-2) + (N-3) + ... + 2 + 1
- Sum 1 through N-1 ---> N(N-1)/2 `(N-1)(N+1-1)/2`

> **Proof** 1 + 2 + ... + n = n(n+1)/2\
Think of a rectangle that has two copies of a triangle of dots (triangle is visual representation of `sum 1 to n`)\
rectangle area is `n(n+1)` and half that to get the sum of the arithmetic sequence)

Example 8
- algorithm takes in array of strings, sort each string, then the full array
- s length of longest string, a length of the array
- key: take into account string comparison takes O(s) time, not O(1) with integer comparison
- sort each string (a strings, at most s lenght) -> a*slogs
- sort the array, ACCOUNT FOR str comparison take O(s) time, there are O(aloga) comparison!
- `O(a*s(loga + logs))`

Example 9
- `2^depth = 2^(log_2(N)) = N (number of nodes)`

Example 10
- Prime number by checking divisibility
- Check till √n because a larger factor of n must be a multiple of a smaller factor that has been already checked
- `O(sqrt(N)) = O(N^(1/2))`

Example 12
- Count all Permutations of a string
- n! leaves and each leaf attached to path of n length
- know no more than `n * n!` nodes
- each node in call tree does O(n) work (recall working with strings here...) -> runtime `O(n^2 * n!)`

> Note branching factor not constant in this viz. This is bc in permutation generation start with x characters in string, in first slot, have 7 choices, once picked, only have 6 choices for the next slot!

Example 13

- Nth Fibonacci , can use `O(branches^depth)`
- go as deep as N

Example 14

- Print all fibonacci numbers
- note NOT O(n2^n), n is changingg
- fib(4) -> 2^4 steps
- **Formula:** T(n) = T(n-1) + T(n-2)
- `2^1 + 2^2 + ... + 2^n` -> 2^(n+1) - 1 -> `O(2^n)`

Example 15

- Memoized fibonacci
- think of tree being snipped, less nodes, less computation
- `O(N)`

## Additional Problems

VI.10
- code that sums the digits in a number
- runtime is # of digits in the number, number with d digits can have a value up to 10^d (excluding)
- n = 10^d -> d = logn
> Note, think of it has **reducing problem space into 1/10th of previous**. Like binary search which is logn
