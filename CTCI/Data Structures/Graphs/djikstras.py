'''

Djikstra's shortest path algorithm

Shortest path from a single source vertex to all other vertices in the given graph

Algorithm
    1. sptSet to track vertices included in shortest path tree, (whose min distance from sourec is calculated and finalized)
    2. Assign distance val to all vertices in input graph, init with INFINITE, assign distval as 0 for source vertex so that picked first
    3. while sptSet doesn't include all vertices...
        a. pick vertex which is not in sptSet and has minimum distance value
        b. include u to sptSet
        c. Update dist val for all adjacent vertices of u. To update, iterate through all adj vertices, 
            for each adj vertex v, if sum of dist val of u (from source) and weight of edge u,v is less than distance value of v, update dist val v


NOTE: Greedy algorithm - An algorithmic paradigm that follows the problem solving heuristic of making the locally optimal choice at each stage with the hope of finding a global optimum
    * Proving greedy algorithm is optimal
        * prove never make a bad choice, greedy can't backtrack -> always need to make the right choice
        * PROOF: algorithm's sequence of choices so far matches a prefix of one of the optimal solutions

NOTE: Dynamic programming - Method to solve a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, 
    and storing their solutions

Greedy or DP?
    It's greedy because you always mark the closest vertex. It's dynamic because distances are updated using previously calculated values.
    Considered a greedy algorithm because it picks the local optimum at each step
    Confusion stems from the fact that Djikstras Algorithm may check multiple routes and “recalculate” old routes when new edges are checked

'''

'''
ADJACENCY MATRIX REPRESENTATION

NOTE: to calculate path info, parent arr, update when distance is updated
NOTE: same djikstra func can be used for directed graphs as well

NOTE: Djikstra's doesn't work for graphs with negative weight cycles
    *** WHY? ***
        Djikstra's assumes paths can only become heavier.
        Pat A-(3)->B and path A-(3)->C, no way you can add an edge and get from A to B through C with a weight of less than 3 
        Assumption helps make the algorithm faster than algos that take negative weights into account
            Assume each vertex in sptSet is minimal, can do relaxation step without looking back

            Bellman-Ford offers recursive DP soln to account for negative weights


'''
# [TIME]  O(V^2)
# [SPACE] O(V)

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]
    
    def printSoln(self, dist):
        print("Vertex \tDistance from Source")
        for vertex in range(self.V):
            print(f'{vertex} \t{dist[vertex]}')
    
    def minDistance(self, dist, sptSet):
        # find vertex with min distance from set of vertices not yet included in shortest path
        min = float('inf')
        minIndex = -1
        for v in range(self.V):
            if sptSet[v] == False and dist[v] < min:
                min = dist[v]
                minIndex = v
        return minIndex
    
    def djikstraAdjMatrix(self, src):
        dist = [float('inf')]*self.V
        dist[src] = 0
        sptSet = [False]*self.V

        # will need to loop through n times to add all vertices to sptSet
        for vertex in range(self.V):
            # find vertex with min distance from set that's not yet processed
            # first iteration, u always equal to src
            v = self.minDistance(dist, sptSet) # NOTE: O(v)

            # TODO: if none found, no valid paths to remaining vertices that aren't in sptSet (disconnected graphs)
            if v < 0:
                break

            sptSet[v] = True
            
            # update dist val of adj vertices of curr min distance vertex to be added to frontier
            # only update if new distance < curr dist and adj not already in sptSet frontier
            
            # NOTE: inner loop O(v) too just to find neighbours using adj matrix --> O(v^2)
            for u in range(self.V): 
                if sptSet[u] == False and self.graph[v][u] > 0 and dist[v] + self.graph[v][u] < dist[u]:
                    dist[u] = dist[v] + self.graph[v][u]
        
        self.printSoln(dist)


# Driver program
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]]
  
g.djikstraAdjMatrix(0);              


            
'''
ADJACENCY LIST REPRESENTATION

NOTE: to calculate path info, parent arr, update when distance is updated
NOTE: same djikstra func can be used for directed graphs as well

NOTE: Djikstra's doesn't work for graphs with negative weight cycles

NOTE: Improvements with adjacency list
    * lists only have adjacent neighbours for each vertex, don't need traverse all vertices
        * All vertices of graph can be traversed in O(V+E) time using BFS
    * Improve runtime to find minDistance by using a minHeap

Algorithm
    1. Create min heap of size v (num of vertices) in given graph. each node is tuple of vertex # and distance val from src
    2. Init min heap with src vertex as root (dist = 0), rest vertices are float("inf")
    3. While min heap is not empty
        * Extract min vertex u
        * For every adj vertex v of u, if v in min heap and curr distance value for v is > weight(u,v)+dist(u) -> update dist(v) 

MAXIMUM number of edges in directed/undirected graph?
    In an undirected graph (excluding multigraphs), the answer is n*(n-1)/2. 
    In a directed graph an edge may occur in both directions between two nodes, then the answer is n*(n-1).

    BFS
        For an undirected graph, each edge will appear twice. 
        Once in the adjacency list of either end of the edge. 
        So, the overall complexity will be O(V) + O (2E) ~ O(V + E).

[TIME]
    Observe that statements in inner loop executed O(V+E) times similar to BFS
    inner look decrease_key takes O(logV) time
    
    O((V+E)*LogV)

    Now on complete graph |E| >> |V| --> O(ElogV)

[SPACE]
    O(V) 
    space optimization compared to O(V^2) where we push same vertex to heap multiple times with relaxed dist before visiting it
'''


# [SPACE] O()

# NOTE: import heapq as hq <--- NEED TO USE CUSTOM HEAP

# Need to update distances in the heap, therefore need a custom heap that tracks
#  pos/index of each vertex in heap array

class MinHeap:
    def __init__(self):
        # this impl not initialized with a value --> 0 - n-1

        # NOTE: min heap node is [v, dist]

        self.heap_list = []
        self.curr_size = 0
        
        # NOTE: pos to track index of vertex in heap list
        self.pos = [] # assume init when heap list init

        # NOTE: Heap list will be init with 0 as root and INF as remainder
    
    # returns min node
    # def find_min(self):
    #     if self.curr_size > 0:
    #         return self.heap_list[0]
    #     return None

    def is_empty(self):
        return False if self.curr_size > 0 else True


    def sift_up(self, i):
        # while there is a parent element to compare
        while (i-1)//2 >= 0:
            parent = (i-1)//2
            if self.heap_list[i][1] < self.heap_list[parent][1]:

                # update pos, THEN swap
                self.pos[self.heap_list[i][0]] = parent
                self.pos[self.heap_list[parent][0]] = i

                # swap the NODES
                self.heap_list[i], self.heap_list[parent] = self.heap_list[parent], self.heap_list[i]

                # continue sifting up
                i = parent
            else:
                return

    def min_child(self, i):
        # return if only 1 child
        left = (i*2)+1
        right = (i*2)+2
        if right >= self.curr_size:
            return left
        else:
            # return index of min child
            return left if self.heap_list[left][1] < self.heap_list[right][1] else right
    
    # [MIN_HEAPIFY]
    def sift_down(self, i):
        # check if curr node has a child
        while (i*2)+1 < self.curr_size: # NOTE: complete binary tree, levels filled LEFT to RIGHT
            # get index of min child
            mc = self.min_child(i)
            # compare & swap if curr > mc
            if self.heap_list[i][1] > self.heap_list[mc][1]:

                # update pos, THEN swap
                self.pos[self.heap_list[i][0]] = mc
                self.pos[self.heap_list[mc][0]] = i
                
                # swap the NODES
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]

            i = mc
            # NOTE: could return here too instead of continue loop

    # NOTE: Don't need insert, will be init another way

    # def insert(self, k):
    #     # append el to bottom rightmost of heap
    #     self.heap_list.append(k)
    #     # append size
    #     self.curr_size += 1

    #     # move element to correct pos from bottom -> top
    #     self.sift_up(self.curr_size-1)

    #  [EXTRACT MIN]
    def extract_min(self):
        # check empty
        if self.curr_size == 0:
            return None
        # get root / min value of heap
        root = self.heap_list[0]

        # update pos, THEN swap
        self.pos[self.heap_list[0][0]] = self.curr_size-1
        self.pos[self.curr_size-1] = 0

        # move last value of heap to root
        self.heap_list[0] = self.heap_list[self.curr_size-1]

        # pop value since copy moved to root? and decrease size of heap
        self.heap_list.pop()
        self.curr_size -= 1
        # sift down the root
        self.sift_down(0)
        # return min val
        return root
    
    def decrease_key(self, v, dist):
        # decrease vertex v's dist in min heap to new dist
        
        # NOTE: Get index of v in heap array, find node and update dist val, siftUp to heapify
        i = self.pos[v]
        
        self.heap_list[i][1] = dist
        self.sift_up(i)

    def is_in_min_heap(self, v):
        if self.pos[v] < self.curr_size:
            return True
        return False

from collections import defaultdict

class Graph2:
    def __init__(self, vertices):
        self.V = vertices
        
        # FORMAT of adjaceny list {(dest, weight), ...}
        self.graph = defaultdict(list)
    
    # NOTE: Graph is undirected
    def addEdge(self, src, dest, weight):
        self.graph[src].append((dest, weight))
        self.graph[dest].append((src, weight))
    
    def printSoln(self, dist):
        print("Vertex \tDistance from Source")
        for vertex in range(self.V):
            print(f'{vertex} \t{dist[vertex]}')
    
    
    def djikstraAdjList(self, src):
        
        # minHeap store remaining vertices not in sptSet
        # dist will eventually store finalized min dist
        dist = []
        # NOTE: sptSet = [False]*self.V
            # Don't need boolean sptSet, can use isInMinHeap to check if dist finalized for a vertex

        minHeap = MinHeap()
        for v in range(self.V):
            dist.append(float("inf"))
            # init minHeap with all INF dist vals, init src with 0
            # heap node list = [v, dist], CANNOT use tuple, need to be mutable
            minHeap.heap_list.append([v, dist[v]])
            minHeap.pos.append(v)
        
        minHeap.curr_size = self.V
        
        dist[src] = 0
        minHeap.decrease_key(src, dist[src])

        # while minHeap is not empty
        while not minHeap.is_empty():
            # extract min vertex u, update dist, sptSet
            minNode = minHeap.extract_min()
            u = minNode[0]
            # for each adj vertex v still in MinHeap, if curr dist > new path dist(u)+weight(u,v), update dist(v)
            for adjVertex in self.graph[u]:
                v = adjVertex[0]
                if minHeap.is_in_min_heap(v) and dist[v] > dist[u] + adjVertex[1]:
                    dist[v] = dist[u] + adjVertex[1]
                    # NOTE: need to update new distance in heap as well
                    minHeap.decrease_key(v, dist[v])
        
        self.printSoln(dist)


graph = Graph2(9)
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

graph.djikstraAdjList(0)


'''

[Djikstra's Using heapq module]

heapq doesn't support decrease_key operation
soln is to NOT update a key, but insert a NEW copy of it with relaxed distance

We only consider node with minimum distance 

[TIME] 
    O(ElogV), at most O(E) vertices in priority queue and O(logE) is same as O(logV)

Further optimization
    Add flag array to store all vertices that have been extracted
    Avoid updating weights of items that have already been extracted

    NOTE: This ensures we only process a vertex once, for loop iterates over outgoing edges
          Among all iterations of while loop, body of for loop runs at most O(E) times

          O(ElogE)
    
    NOTE: Even without optimization, number of nodes in heap bounded by |E|
        Actually (n-1) + (n-2) + (n-3) + ... + 3 + 2 + 1 new edge nodes added every iteration since 
        after ith iteration, i vertices have been processed with finalized min distances

'''