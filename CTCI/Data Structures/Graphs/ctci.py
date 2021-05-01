'''
Graphs
    - Tree is a connected graph without cycles

Connected Graph
    - Path between every pair of vertices

'''

# Two ccommon ways to represent a graph

'''
Adjacency List

    Each vertex/node stores a list of adjacent vertices
    In undirected graph, edge like (a, b) would be stored twice

'''
'''
Adjacency Matrix
    
    nxn boolean matrix wherre n is number of nodes
    true value at matrix[i][j] indicates an edge from node i to node j
    in undirected graph, adj matrix will be symmetric

'''

'''
Graph Search (BFS & DFS)
'''

# Depth-first search
'''
Note pre-order forms of tree traversal are a form of DFS
Check visited nodes to avoid infinite loop

void search(Node root) {
    if (root == null) return
    visit(root)
    root.visited = true
    for each (Node n in root.adjacent) {
        if (n.visited == false) {
            search(n)
        }
    }
}
'''

# Breadth-first search
'''
BFS is iterative with queue not recursive using stack (not intuitive) !!!

void search(Node root) {
    Queue queue = new Queue()
    root.marked = true
    queue.enqueue(root) // add to end of queue

    while (!queue.isEmpty()) {
        Node r = queue.dequeue() // remove from front of the queue
        visit(r)
        for each(Node n in r.adjacent) {
            if (n.marked == false) {
                n.marked = true
                queue.enqueue()
            }
        }
    }
}
'''

# Bidirectional Search
'''
Used to find shortest path between a SOURCE and DESTINATION node

Works by simulatenously running 2 BFS starting from each node, when collide, found path

Why is it faster?

    In traditional bfs, search up to k nodes in first level, up to k nodes for each of the k in second level -> k^2
    O(k^d) nodes where d is length of shortest path from node s to t

    bidirectional, searches collide after d/2 levels (midpoint of path). 
    Search from s ~ k^d/2 nodes, as does search from t --> 2k^d/2 --> O(k^d/2)
        NOTE: recall (k^d/2)*(k^d/2) = k^d --> bidirectional search faster by a factor of k^d/2

    

'''