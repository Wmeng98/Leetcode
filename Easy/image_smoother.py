'''
IMAGE SMOOTHER

Given a 2D integer matrix M representing the gray scale of an image, 
you need to design a smoother to make the gray scale of each cell becomes 
the average gray scale (rounding down) of all the 8 surrounding cells and itself. 
If a cell has less than 8 surrounding cells, then use as many as you can.

M: List[List[int]]
'''
def imageSmoother(M):
    # for each cell in the grid, look at the immediate neighbors - up to 9 of them, including the original cell
    R, C = len(M), len(M[0])
    output = [[0]*C for _ in M]

    for i in xrange(R):
        for j in xrange(C):
            # smooth the cell
            sum = 0
            count = 0

            for nr in (i-1,i,i+1):
                for nc in (j-1,j,j+1):
                    if 0 <= nr < R and 0 <= nc < C:
                        # valid neighbor
                        output[i][j] += M[nr][nc]
                        count += 1
            # smooth the cell by take average across neighbors including cell itself
            # divide once all neighbor grayscales have been aggregated
            output[i][j] /= count
    return output
                