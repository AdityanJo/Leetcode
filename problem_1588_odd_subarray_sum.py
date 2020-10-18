class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        tot=0
        for i in range(1,len(arr)+1,2):
            # tot+=sum([seq for seq in range(len(arr/i))])
            tot+=sum([sum(arr[idx:idx+i]) for idx in range(0,len(arr)-i+1)])
        return tot
