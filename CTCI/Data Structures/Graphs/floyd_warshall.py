'''

floyd warshall

all pair shortest path problem
    * graph[i][j] = 0 if i == j
    * graph[i][j] = inf if there is no edge from vertex i to j

shortest distance matrix

algorithm
    * init soln matrix, update by considering all vertices as intermediate vertex
    * one by one pick all vertices and update shortest paths which include picked vertex as an intermediate vertex
        in the shortest path
    
    * For every pair of (i,j) vertices, there are two cases
        1. k is not intermediate vertex in shortest path from i to j. keep val of dist[i][j] as is
        2. k is intermediate vertex in shortest path from i to j. Update value of dist[i][j] as dist[i][k] + dist[k][j] if dist[i][j] > dist[i][k] + dist[k][j]


[TIME] O(V^3)

NOTE: To print shortest paths, store predecessor/parent info in a separate 2D matrix

'''

def floydWarshall(graph, V):
    # init soln matrix same as input graph
    # NOTE: initial vals of shortest distances are based on shortest paths considering no intermediate vertices

    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    # After kth iteration, vertex k is added to set of intermediate vertices that have been considered {0,1,2,...,k}
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # pick all src,dest vertex pairs
                
                #  If k is on shortest path from i to j then update dist[i][j]
                if dist[i][k] != float('inf') and dist[k][j] != float('inf') and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist


# Driver program to test above
graph = [[0, 5, float('inf'), 10],
         [float('inf'), 0, 3, float('inf')],
         [float('inf'), float('inf'), 0,   1],
         [float('inf'), float('inf'), float('inf'), 0]
         ]
# Print the solution
matrix = floydWarshall(graph, 4)

print('Shortest distance matrix')
print(matrix)