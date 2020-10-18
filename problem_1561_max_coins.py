class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        total=0
        # arranged=sorted(range(len(piles)),key=piles.__getitem__)
        piles.sort()
        for i in range(len(piles)//3):
            total+=piles[len(piles)-2*i-2]
        return total
