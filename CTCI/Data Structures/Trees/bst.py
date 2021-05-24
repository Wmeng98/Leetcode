'''

BINARY SEARCH TREE

* The left subtree of a node contains only nodes with keys lesser than the node’s key.
* The right subtree of a node contains only nodes with keys greater than the node’s key.
* The left and right subtree each must also be a binary search tree. 
* There must be no duplicate nodes.

'''

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

'''
SEARCH

[RUNTIME] O(logn)
'''
def search(root, key):
    # base case - root is none or base case at root
    if root is None or root.val == key:
        return root
    # key is smaller    
    if key < root.val:
        return search(root.left, key)
    #  o/w key greater
    return search(root.right, key)

def searchIterative(root, key):
    curr = root
    parent = None

    if root is None:
        return root
    
    while curr:
        parent = curr
        if curr.val == key:
            return curr
        
        if key < curr.val:
            curr = curr.left
        else:
            curr = curr.right
    return curr


'''
INSERT
    * start at root
    * recurse on left if val of node < root or right if >
    * when reach leaf node, insert at either left/right side

[RUNTIME] O(logn)
'''
# [INSERTION] traverse from root to leaf (new node always inserted as leaf node)
def insert(root, key):
    # base case - always if root is None
    if root is None:
        return Node(key)
    #  o/w recurse & insert at either left/right
    if root.val < key:
        root.right = insert(root.right, key)
    else: 
        root.left = insert(root.left, key)
    return root

def insertIterative(root, key):
    curr = root
    parent = None # store parent of curr node

    # base case - root is None
    if root is None:
        # if tree is empty, create new node and set as root
        return Node(key)
    
    while curr:
        parent = curr

        if curr.val < key:
            curr = curr.right
        else:
            curr = curr.left
    # assign new Node to left/right child of leaf
    print(key)
    node = Node(key)
    if parent.val < key:
        parent.right = node
    else:
        parent.left = node
    return root

'''
DELETE

3 possibilities arise when deleting a node
    1. Node to be deleted is the leaf
        simply remove the node
    2. Node to be deleted only has one child
        Remove node and replace it with its child
    3. Node to be deleted has two children
        Find inorder successor/predecessor of the node and
        copy content and delete the inorder successor/pred

[RUNTIME] O(logn) --> skewed BST O(n)
'''

def deleteNode(root, key):
    # first we need to find the actual node to be deleted
    
    # base case
    if root is None:
        return root
    if key < root.val:
        # key lies in left subtree
        root.left = deleteNode(root.left, key)
        return root
    elif key > root.val:
        # key lies in right subtree
        root.right = deleteNode(root.right, key)
        return root 
    else:
        # key is same as root, found node to be deleted

        # ****** If node has 1 child or no children
        if root.right is None:
            temp = root.left
            root = None # Needed to unreference this memory, is this really needed?
            return temp
        if root.left is None:
            temp = root.right
            root = None # Needed to unreference this memory, is this really needed?
            return temp
        
        # ****** o/w node has 2 children
        # inorder successor - smallest in right subtree
        # NOTE: track the parent of successor to AVOID recursive call to delete successor
        #       NOTE: Successor/Predecessor won't always be a LEAF NODE
        # find the successor
        parent = root
        succ = root.right
        while succ.left is not None:
            parent = succ
            succ = succ.left
        
        if parent != root:
            # succ will be leftmost, assign succ.right to parent.left
            parent.left = succ.right
        else:
            # immediate right of root is succ
            parent.right = succ.right
        
        # COPY succ data to root
        root.val = succ.val
        
        return root

def findSucc(root):
    # ASSUME: root has 2 children
    curr = root.right
    while curr.left is not None:
        parent = curr
        curr = curr.left
    return parent, curr

def deleteNodeIterative(root, key):
    # search for node to be deleted
    curr = root
    while curr is not None:
        parent = curr
        if key < curr.val:
            curr = curr.left
        elif key > curr.val:
            curr = curr.right
        else:
            break
    
    if curr is None:
        return root
    
    # o/w found node to be deleted

    # CASE: node has 1 or 0 children
    if curr.left is None:
        temp = curr.right
        curr = None
        if parent.right is curr:
            parent.right = temp
        else:
            parent.left = temp
    elif curr.right is None:
        temp = curr.left
        curr = None
        if parent.right is curr:
            parent.right = temp
        else:
            parent.left = temp
    else:
        # CASE: node has 2 children, find inorder successor
        succParent, succ = findSucc(curr)
        # if succ is immediate curr.right
        if succParent is curr:
            succParent.right = succ.right
        else:
            # succ will be leftmost, assign succ.right TO parent.left
            succParent.left = succ.right
        
        # cpy succ data to curr
        curr.val = succ.val

    return root

'''
INORDER Traversal
'''
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.val, ',', end="")
    inorder(root.right)


# DRIVER CODE

keys = [15, 10, 20, 8, 12, 16, 25]

root = None
for key in keys:
    root = insertIterative(root, key)

print('search BST:', search(root, 25).val)
print('searchIterative 25 BST:', searchIterative(root, 25).val)
print('delete node(25) from BST...', )
deleteNode(root, 25)
print('searchIterative 25 BST:', searchIterative(root, 25))
print('deleteNodeIterative node(15) from BST...', )
deleteNodeIterative(root, 15)
print('searchIterative 15 BST:', searchIterative(root, 25))
print('inorder traversal:')
inorder(root)



'''
ADVANTAGES of BST over HASH TABLES

* We can get all keys in sorted order by just doing Inorder Traversal of BST. This is not a natural operation in Hash Tables and requires extra efforts.

* Doing order statistics, finding closest lower and greater elements, doing range queries are easy to do with BSTs. Like sorting, these operations 
    are not a natural operation with Hash Tables.

* BSTs are easy to implement compared to hashing, we can easily implement our own customized BST. To implement Hashing, we generally rely on libraries provided by programming languages.

* With Self-Balancing BSTs, all operations are guaranteed to work in O(Logn) time. But with Hashing, Θ(1) is average time and some particular operations may be costly, 
    especially when table resizing happens.

'''