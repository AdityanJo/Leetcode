import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        return sorted(count, key=count.get, reverse=True)[:k]
        # print([i for i in count ])
