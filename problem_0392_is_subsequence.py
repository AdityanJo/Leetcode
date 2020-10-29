class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        if t=="":
            return False
        opt=[[0 for _ in range(len(t))] for _ in range(len(s))]
        s_len=len(s)
        t_len=len(t)
        for i in range(s_len):
            for j in range(t_len):
                if i==0 and j==0 and s[i]==t[j]:
                    opt[i][j]=1
                if s[i]==t[j]:
                    opt[i][j]=opt[i-1][j-1]+1
                else:
                    opt[i][j]=max(opt[i-1][j],opt[i][j-1])
        return True if opt[-1][-1]==min(s_len,t_len) else False
