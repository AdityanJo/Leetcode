class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        out=[]
        for num, idx in zip(nums,index):
            out=out[:idx]+[num]+out[idx:]
        return out
