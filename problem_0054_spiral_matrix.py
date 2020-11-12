class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix==[]: return []
        mode=0
        m,n=len(matrix),len(matrix[0])
        result = []
        while matrix:
            m,n=len(matrix),len(matrix[0])
            # print(m,n)
            if m==0 or n==0:
                break
            # print(matrix)
            if mode==0:
                result+=matrix[0]
                del(matrix[0])
                mode=1
            elif mode==1:
                result+=[matrix[i][-1] for i in range(m)]
                for row in matrix:
                    del(row[-1])
                mode=2
            elif mode==2:
                result+=matrix[-1][::-1]
                del(matrix[-1])
                mode=3
            elif mode==3:
                result+=[matrix[i][0] for i in range(m)][::-1]
                for row in matrix:
                    del(row[0])
                mode=0
        return result
