'''

Prim's Minimum Spanning Tree (MST)

GREEDY ALGORITHM

Spanning Tree
    Subset of graph G which has all the vertices covered with minimum possible number of edges
    * Does not have cycles
    * Cannot be disconnected (it's a tree!!!)

Minimum Spanning Tree
    NOTE: Undirected graph
    Spanning tree whose weight is smallest among all possible spanning trees


Applications of MST
    Construct highways/railroads spanning several cities
    Designing local area networks
    Laying pipelines connecting offshore drilling sites
    Supply a set of houses with Electricity, Water, Telephone

    NOTE: To reduce cost, connect houses with MST. MINIMIZE total length of wire connecting customers 

Prims/Kruskal's Fail on directed graphs
    This is because not all vertices may be CONNECTED in a directed graph
    NOT all nodes reachable from every other node

Prim's can handle negative weights though
    Only consider minimum edge weight
    NOT shortest path like djikstra's

'''

'''
ADJACENCY MATRIX

Impl similar to djikstra's
    * mstSet: bool arr to rep set of vertices included in MST
    * keys: store key values (min weight edge) to pick in cut
    * parent: store indexes of parent nodes in MST

[TIME] O(V^2)
'''


'''
ADJACENCY LIST

Prim’s algorithm, two sets are maintained, one set contains list of vertices already included in MST, other set contains vertices not yet included

With adj list rep, can traverse graph O(V+E) using bfs,
    Traverse all vertices using bfs, 
        use MinHeap to store vertices not yet included in MST, MinHeap is priority queue to get min weight edge from the cut

Impl
    * Could use custom min heap which a decrease_key operation + track pos index of each node in the heap 
        O(ElogV)
    * Or use heapq but tradeoff space for simplicity 
        O(VlogE) + O(ElogE) -> O(ElogE)


NOTE: Prim's algo could give differnt solns depending on how you resolve ties
    All solns should give a MST with the same min weight


'''

from collections import defaultdict
import heapq as hq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        
        # FORMAT of adjaceny list {(dest, weight), ...}
        self.graph = defaultdict(list)
    
    # NOTE: Graph is undirected
    def addEdge(self, src, dest, weight):
        self.graph[src].append([dest, weight])
        self.graph[dest].append([src, weight])
    
    def printMST(self, keys, parent, n):
        total = 0
        for v in range(1, n):
            total += keys[v]
            print(parent[v], '-', v, ' weight:', keys[v])
        print('MST weight:', total)
    
    def primMST(self):
        # keys store minimum edge weights for each vertex to parent (edges in the cut)
        keys = [float('inf')]*self.V
        parent = [None]*self.V
        mstSet = [False]*self.V
        mHeap = []

        # set vertex 0 as root of MST, init with weight 0, no parent
        # assume at least 1 node in graph
        root = 0
        keys[root] = 0
        parent[root] = -1

        # (weight, vertex) -> tuple, don't need to update
        mHeap.append((keys[root], root)) # Don't need to heapify, maintained already

        while mHeap:
            # extract min edge weight from curr
            minNode = hq.heappop(mHeap)
            u = minNode[1]
            mstSet[u] = True

            # add/update adj vertex edge weights to cut if find new min weight edge
            for adjNode in self.graph[u]:
                # NOTE: v in form (dest, weight)
                v = adjNode[0]
                weight = adjNode[1]
                if mstSet[v] == False and keys[v] > weight:
                    # update keys, parent, mHeap
                    keys[v] = weight
                    parent[v] = u
                    hq.heappush(mHeap, (weight, v))
        
        self.printMST(keys, parent, self.V)

# Driver program to test the above functions
graph = Graph(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
graph.primMST()
                    