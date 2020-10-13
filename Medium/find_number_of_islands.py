from collections import deque

class Graph:
    def __init__(self, r, c, g):
        self.row = r
        self.col = c
        self.graph = g
    # helpler to determine if valid cell to run DFS on
    def validCell(self, i, j, visited):
        # needs to be within bounds of matrix and unvisited
        # NOTE: Make sure value of cell is 1 - valid land!!!
        if 0 <= i < self.row and 0 <= j < self.col and not visited[i][j] and self.graph[i][j]:
            return True
        return False

    # dfs
    def DFS(self, visited, i, j):
        # use recursion for DFS
        # mark cell as visited
        visited[i][j] = True

        rowNr = [-1,-1,-1,0,0,1,1,1]
        colNr = [-1,0,1,1,-1,-1,0,1]
        # helper func is safe to determine whether we run DFS on a neighbour
        for n in range(len(rowNr)):
            if self.validCell(i + rowNr[n], j + colNr[n], visited):
                self.DFS(visited, i + rowNr[n], j + colNr[n])

    # def method to count # islands
    def countIslands(self):

        # track visited cells with a boolean array
        visited = [[False for c in range(self.col)] for r in range(self.row)]

        # init count as 0 and traverse cells of matrix
        count = 0
        for i in range(self.row):
            for j in range(self.col):
                # check if cell has been visited, o/w inc count and run DFS on the connected component - new island found
                if not visited[i][j] and self.graph[i][j]:
                    print(i,j,visited[i][j])
                    count += 1
                    self.DFS(visited, i, j)
        
        return count


# Driver code from GeeksforGeeks
graph = [[1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 1], 
        [1, 0, 0, 1, 1], 
        [0, 0, 0, 0, 0], 
        [1, 0, 1, 0, 1]] 
  
  
row = len(graph) 
col = len(graph[0]) 
  
g = Graph(row, col, graph) 
  
print("Number of islands is:")
print(g.countIslands())