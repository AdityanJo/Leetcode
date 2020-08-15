class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0: return ""
        min_length=min([len(s) for s in strs])
        # print(min_length)
        prefix=""
        for i in range(min_length):
            chars=set([s[i] for s in strs])
            if len(chars)!=1:
                return prefix
            else:
                prefix=prefix+list(chars)[0]
        return prefix
                
