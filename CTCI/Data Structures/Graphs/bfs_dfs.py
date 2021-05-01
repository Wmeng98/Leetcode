# bsf
'''

- unlike bfs for a tree, graphs can contain cycles
- for simplicity, assume connected

bfs using recursion?
    trying to use call stack as auxillary storage (queue) is not intuitive nor correct
    at that point, basically doing a dfs

NOTE: with disconnected graph, can just run bfs on all nodes one by one

'''

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        # Use adjaccency list to represent graph
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        # Use boolean array to track visited vertices
        # NOTE: could also use a set 
        visited = [False] * len(self.graph)
        # Queue for BFS
        queue = deque()

        # mark source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Assuming that vertices are identified by integers 1...n

        while queue:
            # dequeue vertex and print it
            v = queue.popleft()
            print(v)

            # get adjacent verticecs, if not visited, mark it and enqueue
            for adj in self.graph[v]:
                if not visited[adj]:
                    visited[adj] = True
                    queue.append(adj)

# Driver code 
  
# Create a graph given in 
# the above diagram 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)") 
g.BFS(2) 

# Time: O(V+E) --> in a complete graph, |edges| >= |vertices|
# Space: O(|V|) = O(b^d) where b is branching factor and d is depth



# dfs
'''

Start at arbitrary root node, explores as far as possible along each branch before backtracking
'''
# Time: O(V+E)
# Space: O(V)
'''
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

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        # Mark as visited
        visited.add(node)
        # Recur on all its adjacent nodes
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def dfs2(visited, graph, node):
    print(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.add(neighbour)
            dfs2(visited, graph, neighbour)
    
def dfsiterative(graph, node):
    visited = set()
    stack = deque()

    # insert root to stack, should be visited if in stack
    stack.appendleft(node)

    while stack:
        # stack many contain the same vertex twice
        # NOTE: nodes in a queue on bfs are all visited, this isn't the case for nodes in the stack!!!!!
        s = stack[-1]
        stack.popleft()

        if s not in visited:
            print(s)
            visited.add(s)
        
        for neighbour in graph[s]:
            if neighbour not in visited:
                stack.appendleft(neighbour)


dfs(visited, graph, 'A')
print('dfs2:')
visited = set()
dfs2(visited, graph, 'A')


'''
applications of bfs vs. dfs

dfs
    * dfs on unweighted graph makes minimum spanning tree
    * detect cycles using dfs
    * topological sorting can be done using dfs
    * using dfs, can find strongly connected components of a graph

bfs
    * p2p, neighbour nodes
    * search engine crawlers
    * networking, broadcast packets
    * shortest path in unweighted graph

'''