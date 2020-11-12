class Solution:
    def getFreshNeighbors(self, i,j,m,n, grid):
        nxt=[]
        if i-1>=0 and grid[i-1][j]==1:
            nxt.append((i-1,j))
            grid[i-1][j]=2
        if j-1>=0 and grid[i][j-1]==1:
            nxt.append((i,j-1))
            grid[i][j-1]=2
        if i+1<=m-1 and grid[i+1][j]==1:
            nxt.append((i+1,j))
            grid[i+1][j]=2
        if j+1<=n-1 and grid[i][j+1]==1:
            nxt.append((i,j+1))
            grid[i][j+1]=2
        return nxt

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten=[(i,j) for i, row in enumerate(grid) for j,orange in enumerate(row) if orange==2]
        fresh=[(i,j) for i, row in enumerate(grid) for j,orange in enumerate(row) if orange==1]
        iteration=-1
        m,n=len(grid),len(grid[0])
        while rotten:
            iteration+=1
            tmp=[]
            # print(rotten)
            for i,j in rotten:
                nxt=self.getFreshNeighbors(i,j,m,n,grid)
                fresh=[pair for pair in fresh if pair not in nxt]
                tmp+=nxt
            rotten=tmp

        if len(fresh)!=0:
            return -1
        else:
            return iteration if iteration!=-1 else 0
