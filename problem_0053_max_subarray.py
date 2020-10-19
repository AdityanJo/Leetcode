class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return nums[0]
        opt=[nums[0]]
        max_val=nums[0]
        for i in range(1,len(nums)):
            opt.append(max(nums[i],nums[i]+opt[i-1]))
            if opt[-1]>max_val:
                max_val=opt[-1]
        return max_val
