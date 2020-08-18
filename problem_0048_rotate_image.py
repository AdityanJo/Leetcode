class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size=len(matrix)
        for i in range(size):
            for j in range(size):
                if i==j: break
                tmp=matrix[j][i]
                matrix[j][i]=matrix[i][j]
                matrix[i][j]=tmp
        for i in range(size):
            matrix[i]=matrix[i][::-1]
        #print(matrix)
        #levels  = len(matrix)
        #for i in range(levels//2):
        #    level_length=levels-(i+1)
        #    print('Level length',level_length)
        #    for j in range(levels-(i+1)):
        #        print(i,i+j)
