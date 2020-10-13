# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        # Use adjaccency list to represent graph
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        # Use boolean array to track visited vertices
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

# Time: O(V+E)
# Space: O(|V|) = O(b^d) where b is branching factor and d is depth

'''
Note that the above code traverses only the vertices reachable from a given source vertex. 
All the vertices may not be reachable from a given vertex (example Disconnected graph). 
To print all the vertices, we can modify the BFS function to do traversal starting from all nodes one by one
'''