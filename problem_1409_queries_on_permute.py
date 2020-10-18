class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P=list(range(1,m+1))
        out=[]
        for i, query in enumerate(queries):
            idx=P.index(query)
            del(P[idx])
            P=[query]+P
            out.append(idx)
        return out
