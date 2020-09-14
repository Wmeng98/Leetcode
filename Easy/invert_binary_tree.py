# Solution 1 - Recursive approach
#  - top down recursion to inverse children before parent
#  - O(n) runtime where n is # nodes and O(h) space where h is height of the tree

def recursiveInvert(root):
    # check base case
    if root == None:
        return root
    
    inverseRight = recursiveInvert(root.right)
    inverseLeft = recursiveInvert(root.left)

    root.left = inverseRight
    root.right = inverseLeft

    return root

# Solution 2 - Iterative
#  - Similar to BFS, nodes on queue mean their children have not been swapped yet
#  - Swap as we go down the tree
#  - O(n) but now O(n) space since queue can contain all nodes in the leaf level roof(n/2)

def IterativeInvert(root):
    if root == None:
        return root

    # Use list to implement a queue
    queue = []
    queue.append(root)
    while len(queue):
        # remove next node from queue
        curr = queue.pop(0)
        
        temp = curr.left
        curr.left = curr.right
        curr.right = temp
        
        if curr.left: queue.append(curr.left) 
        if curr.right: queue.append(curr.right) 
        
    return root