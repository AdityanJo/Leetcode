class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp=''
        max_len=0
        for char in list(s):
            if char not in tmp:
                tmp+=char
            else:
                tmp=tmp[tmp.find(char)+1:]+char
            if len(tmp)>max_len:
                max_len=len(tmp)
            # print(tmp)
        return max_len
        
