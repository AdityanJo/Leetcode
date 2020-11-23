class Solution:
    # def fact(self,n):
    #     if n==0:
    #         return 1
    #     return n*self.fact(n-1)
    # def trailingZeroes(self, n: int) -> int:
    #     factorial = self.fact(n)
    #     factorial = str(factorial)
    #     length = len(factorial)
    #     i=length-1
    #     # print(factorial, factorial[i])
    #     while factorial[i]=='0':
    #         i-=1
    #     return length-i-1
    def trailingZeroes(self, n: int) -> int:
        r=0
        while n>0:
            n=n//5
            # print(n,r)
            r+=n
        return r
