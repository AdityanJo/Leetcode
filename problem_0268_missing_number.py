class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = [0]*(len(nums)+1)
        for num in nums:
            # print(num)
            res[num]+=1
        return res.index(0)
