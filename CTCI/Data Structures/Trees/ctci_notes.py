'''

Trees

- Root node, child nodes, etc.
- Tree cannot contain cycles

'''

'''
### Tree vs. Binary Tree
    - binary tree: each node has up to 2 children
### Binary Search Tree
    - binary tree in which every node fits a specific ordering property
    - (one def'n) all left descendents <= n < all right descendents -----> must hold for each node
    - NOTE: INEQUALITY MUST BE TRUE FOR ALL OF A NODES DESCENDENTS

### Balanced vs. Unbalanced
    - Balanced enough to ensure O(logn) times for insert/find
    - 2 common types of balanced trees are 
        1. red-black trees
        2. AVL trees
    
### COMPLETE Binary Trees
    - every level of tree is filled except perhaps the last level (filled left to right)

### FULL Binary Tree
    - every node has either zero (leaf node) or 2 children

### PERFECT Binary Tree
    - one that is both full and complete
    - all leaf nodes at same level, last level is filled
'''


###############################################################################

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def getTestBinaryTree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    return root


'''
Binary Tree Traversal (in-order, pre-order, post-order)
'''

'''
In-Order Traversal (LEFT, CURRENT, RIGHT node)

void inOrder(node):
    if node != null:
        inOrder(node.left)
        visit(node)
        inOrder(node.right)
'''


'''
Pre-Order Traversal (CURRENT, LEFT, RIGHT node)

void preOrder(node):
    if node != null:
        visit(node)
        preOrder(node.left)
        preOrder(node.right)
'''


'''
Post-Order Traversal (LEFT, RIGHT, CURRENT node)

void postOrder(node):
    if node != null:
        postOrder(node.left)
        postOrder(node.right)
        visit(node)
'''


###############################################################################

'''
Binary Heaps (Min-Heaps & Max-Heaps)

Applications of Heaps
    - HeapSort O(nlogn) time
    - Priority queues, binary heaps support insert,delete,extract_max in O(logn) time
    - Graph algorithms (djikstras, prims, etc) that use priority queues


'''

'''
MIN-HEAP (elements in ascending order)

    - Complete binary tree (totally filled other than the rightmost el of the last level)
        - NOTE: This property makes them suitable to be stored in an array
    - NOTE: each node is smaller than it's children, root therefore is min el of the tree

'''

'''
Implementing Heap using an Array

Starting from 0...n-1
    Arr[(i-1)/2] -> parent node
    Arr[(2*i)+1] -> left child node
    Arr[(2*i)+2] -> right child node

NOTE: The traversal method used to achieve array implementation is level order 
'''

'''
Min-Heap

    Insertion O(logn)
    Delete Min O(logn)
    Find Min O(1)
    Heapify O(n)
        This op rearranges all nodes after deletion or insertion, cost is n since all el need to be moved to keep heap properties
        NOTE: heapify can only be applied to a node if its children nodes are heapified, need to be performed in BOTTOM-UP ORDER
    Delete Node O(logn)

'''

class MinHeap:
    def __init__(self):
        # this impl not initialized with a value --> 0 - n-1
        self.heap_list = []
        self.curr_size = 0
    def find_min(self):
        if self.curr_size > 0:
            return self.heap_list[0]
        return None

    def sift_up(self, i):
        # while there is a parent element to compare
        while (i-1)//2 >= 0:
            parent = (i-1)//2
            if self.heap_list[i] < self.heap_list[parent]:
                # swap them
                self.heap_list[i], self.heap_list[parent] = self.heap_list[parent], self.heap_list[i] 
                # continue sifting up
                i = parent
            else:
                return

    def min_child(self, i):
        # return if only 1 child
        left = (i*2)+1
        right = (i*2)+2
        if right >= self.curr_size:
            return left
        else:
            # return index of min child
            return left if self.heap_list[left] < self.heap_list[right] else right
    
    def sift_down(self, i):
        # check if curr node has a child
        while (i*2)+1 < self.curr_size: # NOTE: complete binary tree, levels filled LEFT to RIGHT
            # get index of min child
            mc = self.min_child(i)
            # compare & swap if curr > mc
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i] 
            i = mc
            # NOTE: could return here too instead of continue loop

    def insert(self, k):
        # append el to bottom rightmost of heap
        self.heap_list.append(k)
        # append size
        self.curr_size += 1
        # move element to correct pos from bottom -> top
        self.sift_up(self.curr_size-1)

    def delete_min(self):
        # check empty
        if self.curr_size == 0:
            return None
        # get root / min value of heap
        root = self.heap_list[0]
        # move last value of heap to root
        self.heap_list[0] = self.heap_list[self.curr_size-1]
        # pop value since copy moved to root? and decrease size of heap
        self.heap_list.pop()
        self.curr_size -= 1
        # sift down the root
        self.sift_down(0)
        # return min val
        return root



"""
Driver program
"""
# Same tree as above example.
my_heap = MinHeap()
my_heap.insert(5)
my_heap.insert(6)
my_heap.insert(7)
my_heap.insert(9)
my_heap.insert(13)
my_heap.insert(11)
my_heap.insert(10)

print('MinHeap')
print('min node', my_heap.delete_min()) # removing min node i.e 5 
    

###############################################################################

'''
TRIES (PREFIX TREES)

Trie variant of n-ary tree in which characters are stored at each node
Each path down tree may represent a word

(*) null nodes used to indicate complete words

A node in a trie can have anywhere from 1 through ALPHABET_SIZE + 1 children
Or 0 through ALPHABET_SIZE if a boolean flag is used instead of a * node

Store entire engish language for quick prefix lookups
    trie can check if string is valid prefix in O(k) time
    
    NOTE: Hash table cannot tell us if a string is a prefix of any valid words

'''

###############################################################################

###############################################################################

###############################################################################

###############################################################################
