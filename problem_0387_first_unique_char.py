import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hist=collections.OrderedDict()
        for i, char in enumerate(s):
            if hist.get(char) is None:
                hist[char]=[1,i]
            else:
                hist[char][0]+=1
        for k,v in hist.items():
            if v[0]==1:
                return v[1]
        return -1
