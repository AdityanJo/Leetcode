class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])
        if m==n:
            for i in range(m):
                for j in range(i,n):
                    tmp=A[i][j]
                    A[i][j]=A[j][i]
                    A[j][i]=tmp
            return A
        res = [[0 for _ in range(m)] for __ in range(n)]
        # print(res)
        for i in range(n):
            for j in range(m):
                res[i][j]=A[j][i]
        return res
        
