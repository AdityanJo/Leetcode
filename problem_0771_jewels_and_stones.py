class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels=list(J)
        count=0
        for char in S:
            if char in jewels:
                count+=1
        return count
