class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        tot=0
        for i in range(n):
            if i!=int(n/2) and n%2!=0:
                tot+=mat[i][i]+mat[i][n-i-1]
            elif n%2==0:
                tot+=mat[i][i]+mat[i][n-i-1]
            else:
                tot+=mat[i][i]
        return tot
