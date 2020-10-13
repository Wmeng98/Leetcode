# Simple implementation of DFS search
# https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-pytho

# Graph represented using an adjacency list - dictionary data structure

# Time O(V+E)

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : ['E'],
    'E' : ['F'],
    'F' : ['D']
}

# Track visited nodes
visited = set() 

'''
Time: O(V+E)
Space: O(V)

DFS steps (recursive):

1. recursive func that takes at least the index of a node and visited set
2. if not isn't visited, print node, add to visited set
3. Recur on all its adjacent nodes

DFS steps (iterative):

Only difference is that recursive stack is replaced by a stack of nodes

1. insert root into stack
2. run loop until stack is not empty
3. pop element and print
4. For every adj and unvisited nodes, mark as visited and insert it into the stack


Handling Disconnected Graphs
    Run a loop from 0 to number of vertices and check if the node is unvisited in previous DFS then call the recursive function with current node.

'''

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        # Mark as visited
        visited.add(node)
        # Recur on all its adjacent nodes
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
    

dfs(visited, graph, 'A')