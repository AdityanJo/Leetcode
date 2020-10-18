class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        reg=start
        for i in range(1,n):
            reg=reg^(start+2*i)
        return reg
