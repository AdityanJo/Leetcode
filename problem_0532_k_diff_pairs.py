import collections
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # count = 0
        # pairs=set()
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         diff = nums[i]-nums[j]
        #         if diff!=0 and k==abs(diff) and i!=j:
        #             if (nums[i], nums[j])  and (nums[j],nums[i]) not in pairs:
        #                 pairs.add((nums[i], nums[j]))
        #                 count+=1
        #         if diff==0 and k==diff and i!=j:
        #             count+=1
        #             pairs.add((nums[i], nums[j]))
        #             # print(nums[i], nums[j])
        # # print(pairs)
        # return len(pairs)

        #complement approach
        c = collections.Counter(nums)
        if k==0:
            return sum([c[i]>1 for i in c])
        else:
            return sum([(i+k in c) for i in c])
