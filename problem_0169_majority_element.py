class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2 and nums[0]==nums[1]:
            # print('returning')
            return nums[0]
        else:
            mid = len(nums)//2
            l=self.majorityElement(nums[:mid])
            r=self.majorityElement(nums[mid:])
            # print(nums[:mid], nums[mid:],l,r)
            l_count=0
            r_count=0
            if l is not None:
                if l==r:
                    return l
                l_count=sum([1 for v in nums if v==l])
            if r is not None:
                r_count=sum([1 for v in nums if v==r])
            # print(l_count, r_count)
        return l if l_count>r_count else r