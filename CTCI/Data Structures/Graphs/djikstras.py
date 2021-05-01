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
            v = self.minDistance(dist, sptSet)

            # TODO: if none found, no valid paths to remaining vertices that aren't in sptSet (disconnected graphs)
            if v < 0:
                break

            sptSet[v] = True
            
            # update dist val of adj vertices of curr min distance vertex to be added to frontier
            # only update if new distance < curr dist and adj not already in sptSet frontier
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


            

