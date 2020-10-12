from collection import deque

# Time: O(N) where N is the number of nodes
# Space: O(N) at worst for unevenly distributed 
def get_cheapest_cost(rootNode):
  # start at root 
  # run DFS to get to leaf nodes
  # record cost at leafs and track min path
  
  stack = deque()
  stack.append(rootNode)
  minCost = float('inf')
  # currCost = 0
  while not stack.isEmpty():
    
    # pop and add children back to the stack
    node = stack.pop()
    # add parent cost to child node
    if node.parent:
      node.cost += node.parent.cost
      
    # check if leaf node
    if len(node.children) == 0:
      minCost = min(node.cost, minCost)
      
    # push children onto stack
    for child in node.children:
      stack.push(child)
  
  return minCost
  


# Time: O(N) where N is the number of nodes
# Space: O(N) at worst
def get_cheapest_cost_recursive(rootNode):
  # Can implement DFS with recursion
  # BOTTOM UP RECURSION 
  #    Assume what returns from recursive call is processed
  
  # base case - if reached a leaf node
  if rootNode.children == []:
    return rootNode.val
  
  # o/w recurse on children and find smallest path cost among all children
  # track minCost and update if smaller path found
  minCost = float('inf')
  for child in rootNode.children:
    childCost = get_cheapest_cost_recursive(child)
    minCost = min(childCost, minCost)
    
  return minCost + rootNode.val
      



########################################## 
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node 
class Node:

  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None

    
 