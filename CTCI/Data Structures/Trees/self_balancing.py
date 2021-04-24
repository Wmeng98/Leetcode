'''

Red Black Trees (RB Tree)

Self-balancing binary search tree where each node has an EXTRA BIT
Bit often interpreted as the colour (red or black)
NOTE: Colour used to ensure tree remains balanced during insertions/deletions

Point of balancing tree is to reduce search time and maintain O(logn)

RULES THAT EVERY RB TREE FOLLOWS...
    1. every  node has colour, either red or black
    2. root of tree always black
    3. there are no two adjacent red nodes
    4. Every path from a node (including root) to any of its descendants NULL nodes has the same number of black nodes

NOTE: colour of null node is always black

2 types actions used to rebalance
    - Recolouring
    - Rotations

'''

'''

AVL Trees

Self-balancing BST where difference between heights of left and right subtress cannot be more than one for all nodes

Operations performed to rebalance BST without VIOLATING BST property keys(left) < key(root) < keys(right)
    - Left Rotation
    - Right Rotation

Really 4 cases
    - Left Left Case
    - Left Right Case
    - Right Right Case
    - Right Left Case

'''

'''

RB Tree vs. AVL

AVL more balanced compared to RB tree, but they may cause more rotations during insertion/deletion
NOTE: Choose tree to use depending on the frequency of insertions/deletions


* AVL trees are more rigidly balanced and hence provide faster look-ups. Thus for a look-up intensive task use an AVL tree.

* For an insert intensive tasks, use a Red-Black tree.

* AVL trees store the balance factor at each node. This takes O(N) extra space. However, if we know that the keys that will 
    be inserted in the tree will always be greater than zero, we can use the sign bit of the keys to store the colour information 
    of a red-black tree. Thus, in such cases red-black tree takes no extra space.


'''