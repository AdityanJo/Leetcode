class Solution:
    def isHappy(self, n: int) -> bool:
        hist=set()
        while True:
            n=sum([int(v)*int(v) for v in str(n)])
            if n==1:
                return True
            else:
                if n in hist:
                    return False
                hist.add(n)

        return False
