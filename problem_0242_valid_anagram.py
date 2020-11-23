class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_c=len(s)
        for i in range(s_c):
            # print(i)
            loc = t.find(s[i])
            if loc ==-1:
                return False
            else:
                t= t[:loc]+t[loc+1:]
                s_c-=1
        if t=='' and s_c==0: return True
        else: return False
