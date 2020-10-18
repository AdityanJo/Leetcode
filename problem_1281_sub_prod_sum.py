class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod=1
        tot=0
        while n>0:
            dig=n%10
            prod*=dig
            tot+=dig
            n=int(n/10)
        return prod-tot
