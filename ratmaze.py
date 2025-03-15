def validpath(maze,i,j,m,n):
    if i==m or j==n:
        return False
    if maze[i][j]==1:
        return False
    return True
def ratmaze(maze,i,j,m,n,arr):
    if arr[-1][-1]==1:
        return True
    if validpath(maze,i,j,m,n):
        arr[i][j]=1
        if ratmaze(maze,i+1,j,m,n,arr):
            return True
        if ratmaze(maze,i,j+1,m,n,arr):
            return True
        arr[i][j]=0
    return True
maze=[[0,1,0,1,1],[0,0,0,0,0],[1,0,1,0,1],[0,0,1,0,0],[1,0,0,1,0]]