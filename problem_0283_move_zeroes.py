class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1: return nums
        i = 0; z = 0; n = len(nums)
        while i < n:
            print(z)
            if nums[i]==0:
                z+=1
                del(nums[i])
                i-=1
                n-=1

            i+=1
        for _ in range(z):
            nums.append(0)
