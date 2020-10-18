class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups={s:[] for s in set(groupSizes)}
        for idx,i in enumerate(groupSizes):
            if len(groups[i])!=0 and len(groups[i][-1])<i:
                groups[i][-1].append(idx)
            elif len(groups[i])!=0 and len(groups[i][-1])==i:
                groups[i].append([idx])
            if len(groups[i])==0:
                groups[i].append([idx])
        final=[]
        for i in groups.values():
            [final.append(group) for group in i]
        return final
                
