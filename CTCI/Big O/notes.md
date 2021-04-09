# Big O

Asymptotic analysis (describe limiting behavior) for the estimation of computational complexity.

## Big O, Big Theta, and Big Omega

- big O: upper bound on time/space, O(N) -> at **least** as fast as N
- big omega: lower bound on time/space, Ω(N) -> **wont be faster** than N
- big theta: tight bound on runtime/space, θ(N) -> both O(N) and Ω(N)

## Best, Worst, Expected Case

Best, Worst, Expected cases all describe big O (runtime) for particular inputs/scenarios

## Space Complexity

Stack space (levls of the stack) in recursive calls count for space complexity.\
Note calls need to simultaneously exist on the call stack to take up additional space

## Drop the

- contstants
- non-dominant terms

## Amortized Time

Average running time of an operation

## Log N Runtimes

number of elements in problem space are reduced by some proportion (halved, thirds, etc.)

> Note we drop base for logs because any two logarithms differ by constant factor (by **change of base formula**, logs are constant multiples of one another)

>log𝑎𝑛=Θ(log𝑏𝑛) for all 𝑎,𝑏>1

## Recursive Runtimes

Tree depth vs. height
- For each node in a tree, we can define two features: **height** and depth. A node's height is the number of edges to its most distant leaf node. On the other hand, a node's **depth** is the number of edges **back up to the root**

**floor[log_2(N)]** where N is number of nodes in a binary tree is getting the height of that tree (height)

consider f(n-1)+f(n-1)
- with recursive functions making multiple calls, the runtime will often look like O(branches^depth) -> O(2^N).
- Note that runtime is asymptotic as the formula for the actual # nodes is actually `2^0 + 2^1 + .. + 2^N` which is `2^(N+1) - 1`
- Note space complexity is `O(N)` as only O(N) nodes exist at any given time

> Note base of a log doesn't matter since bases only differ by constant factor. However, this **doesn't apply to exponent bases**. 8^N -> (2^3)^N -> 2^3N -> 2^2N * 2^N and 2^N are differet by a factor of 2^2N **which is not a constant factor**.

