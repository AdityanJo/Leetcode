class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lut={}
        for i, num in enumerate(nums):
            complement=target-num
            idx=lut.get(num)
            if idx is not None:
                return [i, idx]
            lut[complement]=i
