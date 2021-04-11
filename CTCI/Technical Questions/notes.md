# Technical Questions

Logical ways to approach technical q's

## Core DS, Algos, and Concepts

- DS: linked lists, tree, tries, and graphs, heaps, vector, hash table
- Algos: BFS, DFS, binary search, merge sort, quick sort
- Concepts: bit manipulation, memory (stack vs. heap), recursion, DP, big O time & space

## Powers of 2

- A 10-bit address can store 1024 addresses (1KB storage) `2^10 -> 1024 Bytes -> 1KB`
- `2^16 -> 65536 Bytes -> 64KB`
- `2^20 -> 1,048,576 Bytes -> 1MB`
- `2^30 -> 1,073,741,824 Bytes -> 1GB`
- `2^32 -> 4GB`
- `2^40 -> 1TB`

> Note `(2^30)*2*2 -> 2^(30+2) -> 2^32`\
> Note difference between 32-bit address (4 GB) and 2^32 bits of memory which is **2^29 bytes/addresses** `(easier to work with to convert to memory since each address references a byte)` which is `2^30 bytes (1GB) / 2` -> **500MB (half a gigabyte of memory)**

## Walk through the Problem

1. **Listen**\
  a. run repeatedly, sorted, etc.

2. **Draw an Example**\
  a. specific, sufficiently large

3. **State Brute Force**\
  a. steps 2 & 3 swappable

4. **Optimize**\
  a. unused info, fresh example, time vs. space tradeoff, precompute info, hash table\
  b. BCR - best conceivable runtime 

5. **Walk Through**\
  a. don't dive into coding yet with an optimal solution\
  b. pseudocode, not sloppy code (steps 1-4 for ex.)

6. **Implement**\
  a. Write beautiful code\
  b. If confused, go back to example and walk through it again
    > Modularized (fill in func details later)\
  Error checks (//todo is good compromise)\
  Use classes and structs where appropriate (fill in details of class after)\
  Good variable names (can abbreviate on whiteboard)

  7. **Test**\
    a. conceptual\
    b. hot spots (base case in recursion, null nodes, etc.), small test cases, special cases\
    c. when find bug, **ensure your fix is the best one.**

## Optimize & Solve Technique

## 1: Look or BUD

3 of most common things an algorithm can waste time doing

**Bottlenecks**

- one-time work slowing down overall runtime (sorting first)
- chunk of work that's done repeatedly
  - Ex. go from brute force N^2 to binary search (NlogN) to unsorted hash table (time vs. space tradeoff) `O(N)`

**Unecessary Work**

- `a^3 + b^3 = c^3 + d^3`
- remove unecessary nested for loops

**Duplicated Work**

- use (c,d) map directly rather than generate (a.b) pairs again bc they will already be in the map

## 2: DIY

- work through it intuitevly on a real example
- Note optimizations you intuitively or automatically made

  Ex. Given smaller string s and bigger b, find all permutations of the shorter string within the longer one. 

## 3: Simplify and Generalize

- Ex. can ransom note be formed from given magazine? (string)
- Simplify first by `cutting characters out first instead of words`

## 4: Base Case and Build

- solve problem for base case and build up from there
  Ex. print all permutations of string (simplicity assume all char unique)

## 5; Data Structure Brainstorm

- run through list of DS and try to apply each one

## BCR - Best Conceivable Runtime

- **best runtime you can conceive of a solution**
> Note finding all pairs with sum k doesn't have BCR of O(N^2)
- Use to get a hint of what we need to reduce
- Use to indicate we're done in terms of optimizing runtime, turn efforts to space complexity



