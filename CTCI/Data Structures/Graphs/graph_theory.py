# graph theory terminology & lemmas
'''

degree - number of edges touching the vertex

handshaking lemma
    - finite undirected graphs
    - an even number of vertices will have odd degree
    - consequence of the `degree sum formula`
        sum(deg(v el of vertices)) = 2|# edges|

complete graph
    - vertex is connected to all other vertices in a graph
    
cycles
    
    let (v,e) be graph where between 2 vertices v1, v2 there only exists one path, then...
        * graph has no cycles
        * adding a new edge (but not vertex) creates a cycle
    
cyclic, acyclic graphs

bipartite graphs
    two sets of vertices s1 and s2
    if any edge is drawn, it should connect any vertex in set s1 to vertex in set s2

complete bipartite graph
    a bipartite graph is said to be complete if `every` vertex in s1 is connected to `every` vertex in s2

complement of a graph
    if edges exist in graph 1 are absent in graph 2, if both combined together to form a complete graph,
    then graph 1 & 2 are called complements of each other


much more...
    connectivity, coverings, matchings, coloring, isomorphism, traversability (hamilton's path)


'''