class Solution:
    def minOperations(self, n: int) -> int:
        start=1
        end=(2*(n-1))+1
        mid=(start+end)/2
        arr=[((2*i)+1)-mid for i in range(n)]
        return int(abs(sum(arr[:n//2])))
        # grads=[]
        # print(len(arr)//2)
        # for i in range(len(arr)//2):
        #     grads.append(arr[i]-mid)
        # return int(abs(sum(grads)))
