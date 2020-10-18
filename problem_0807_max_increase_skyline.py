class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows=[]
        cols=[]
        for i in range(len(grid)):
            rows.append(max(grid[i]))
            cols.append(max([grid[j][i] for j in range(len(grid))]))
        total=0
        for i in range(len(grid)):
            total+=sum([min(cols[j],max(grid[i]))-grid[i][j] for j, val in enumerate(grid[i])])
        return total
