class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_cpy=nums.copy()
        nums_cpy.sort()
        out=[]
        for i in range(len(nums)):
            out.append(nums_cpy.index(nums[i]))
        return out
