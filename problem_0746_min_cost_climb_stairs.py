class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<=1:
            return sum(cost)
        cost.append(0)
        opt=[cost[0], cost[1]]

        for i in range(2,len(cost)):
            opt.append(min(opt[i-1], opt[i-2])+cost[i])
        return opt[-1]
        
