class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        opt=[1,1]
        for i in range(1,n):
            opt.append(opt[i]+opt[i-1])
        return opt[-1]
