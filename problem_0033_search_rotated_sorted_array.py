class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]<=nums[i-1]:
                break
            if target==nums[i]:
                return i
        beg=i
        end=len(nums)-1
        while beg<=end:
            mid=int((beg+end)/2)
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end=mid-1
            elif nums[mid]<target:
                beg=mid+1
        return -1
