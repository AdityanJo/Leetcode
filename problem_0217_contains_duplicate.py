class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)<=1: return False
        #sol 1
        # hist=set()
        # for num in nums:
        #     if num not in hist:
        #         hist.add(num)
        #     else:
        #         return True
        # return False

        return len(nums)!=len(set(nums))
