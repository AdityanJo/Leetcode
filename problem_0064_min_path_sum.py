class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1:
            return sum(grid[0])
        elif n==1:
            return sum(grid)
        if m==0 and n==0:
            return 0

        for i in range(m):
            for j in range(n):
                if i==0 and j!=0:
                    grid[i][j]+=grid[i][j-1]
                elif i!=0 and j==0:
                    grid[i][j]+=grid[i-1][j]
                elif i==0 and j==0:
                    continue
                else:
                    grid[i][j]=min(grid[i-1][j],grid[i][j-1])+grid[i][j]

        return grid[-1][-1]
