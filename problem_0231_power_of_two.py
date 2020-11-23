class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n<4:
        #     if n in [1,2]:
        #         return True
        #     else:
        #         return False
        # else:
        #     while n>=4:
        #         print(n)
        #         n=n/4
        #     if n==1:
        #         return True
        # return False
        return (n&n-1)==0 and n>0
