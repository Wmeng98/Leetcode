# Simple implementation of DFS search
# https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-pytho

# Graph represented using an adjacency list - dictionary data structure

# Time O(V+E)

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
    

dfs(visited, graph, 'A')