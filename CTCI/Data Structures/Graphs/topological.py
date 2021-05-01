'''
TOPOLOGICAL SORTING

Topological sorting for direct acyclic graph (DAG) is linear ordering of vertices s.t for every
direct edge u v, vertex u comes before vertex v in the ordering

NOTE: Topological sort not possible if graph is NOT a DAG

NOTE: There can be more than one topological sorting for a graph

NOTE: The first vertex in toposort is always a vertex with in-degree 0 (vertex with NO incoming edges)

Can modify DFS to find topological sorting of a graph

Algorithm
    Use temporary stack, don't print vertex immediately,  
    Recursively call toposort on all adjacent vertices, THEN push to stack
    Finally, print contents of the stack

Applications
    Mainly used for scheduling jobs from the given dependencies among jobs

'''

# [TIME]  O(V+E) -> DFS with an extra stack
# [SPACE] O(V) -> recursive stack, then additional temp stack

from collections import defaultdict, deque

class Graph:
    def __init__(self, num_of_vertices):
        self.graph = defaultdict(list)
        self.v = num_of_vertices
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    # recursive function
    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        # recur for all vertices adjacent
        for adj in self.graph[v]:
            if visited[adj] == False:
                self.topologicalSortUtil(adj, visited, stack)
        
        # push current vertex to stack which stores results
        stack.appendleft(v)
    
    def topologicalSortRecursive(self):
        visited = [False]*self.v
        stack = deque()

        # store topological sort starting from all vertices one by one
        for i in range(self.v):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        
        temp_sorted = []
        while stack:
            temp_sorted.append(stack.popleft())
        print('topological sort recursive', temp_sorted)

    # Toposort a little difficult to do iteratively since DFS visits node first then child
    # Could use vector, any new unvisited nodes append to FRONT of list NOT BACK?

    # Can use kahns algorithm - BFS, Removing in-degrees


# Driver Code
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

g.topologicalSortRecursive()