class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res=''
        for i in sorted(range(len(indices)), key=indices.__getitem__):
            res+=s[i]
        return res
