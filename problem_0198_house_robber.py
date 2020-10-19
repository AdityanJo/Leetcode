class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)<=2:
            return max(nums)
        opt=[nums[0],max(nums[0], nums[1]), max(nums[1],nums[0]+nums[2])]
        for i in range(3,len(nums)):
            opt.append(max(opt[i-2]+nums[i],opt[i-1]))
        print(opt)
        return opt[-1]
            
