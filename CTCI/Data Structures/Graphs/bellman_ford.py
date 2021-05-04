'''

Bellman Ford's Algorithm

* Single source shortest path algorithm WITH negative edges and negative cycles
* Similar to Djikstra but works on negative edge weights

Negative Cycle (diff from negative edge weights)
    * A path/cycle where total sum of edge weights in the path is negative
    * Therefore, can circle the cycle as much as we want to reduce the shortest distance

Algorithn
    * outer loop: |V|-1 times
        * inner loop: for each edge u-v
            * if dist[v] > dist[u] + weight(u,v)
                * dist[v] = dist[u] + weight(u,v)
    
    * report if there is negative weight cycle in graph
        * for each edge u-v
            * if dist[v] > dist[u] + weight(u,v) --> "then graph contains negative weight cycle"

    * NOTE: Idea is first step guarantees shortest distances if graph doesn't contain av negative weight cycle

HOW DOES IT WORK?
    Like all DP problems, shortest paths calculated in bottom-up manner
    
    First calc shortest distances which have at-most one edge in path
    Then, calc shortest distances with at-most 2 edges in path
    After ith iteration of outer-loop, shortest paths with at most i edges are calculated

    NOTE: There can be max |V|-1 edges in any simple path, that's why outer loop runs |V|-1 times



[TIME] |E|*(|V|-1) -> O(|V||E|)

'''

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        
        # FORMAT of adjaceny list {(dest, weight), ...}
        self.graph = defaultdict(list)
    
    # NOTE: Graph is DIRECTED in this example
    def addEdge(self, src, dest, weight):
        self.graph[src].append([dest, weight])
        # self.graph[dest].append([src, weight])
    
    def printSoln(self, dist):
        print("Vertex \tDistance from Source")
        for vertex in range(self.V):
            print(f'{vertex} \t{dist[vertex]}')

    def bellmanFord(self, src):
        # init distance from src to all other vertices
        dist = [float('inf')]*self.V
        parent = [None]*self.V

        dist[src] = 0

        # Relax all edges |V|-1 times. Simple shortest path from src to any other vertex an have at-most |V|-1 edges
        for _ in range(self.V-1):

            # 2 inner loops are |E|
            for vertex, edges in self.graph.items():
                for edge in edges:
                    # update dist vals if new min found
                    u = vertex
                    v = edge[0]
                    weight = edge[1]

                    if dist[u] != float('inf') and dist[v] > dist[u] + weight:
                        dist[v] = dist[u] + weight
                        parent[v] = u
        
        # Check for negative weight cycles, above guarantees shortest path if graph doesn't contain negative weight cycle
        for vertex, edges in self.graph.items():
            for edge in edges:
                u = vertex
                v = edge[0]
                weight = edge[1]

                if dist[u] != float('inf') and dist[v] > dist[u] + weight:
                    print('Negative cycle detected')
                    return
        
        self.printSoln(dist)

# Driver program to test above
g = Graph(5) 
g.addEdge(0, 1, -1) 
g.addEdge(0, 2, 4) 
g.addEdge(1, 2, 3) 
g.addEdge(1, 3, 2) 
g.addEdge(1, 4, 2) 
g.addEdge(3, 2, 5) 
g.addEdge(3, 1, 1) 
g.addEdge(4, 3, -3) 
        
g.bellmanFord(0) 