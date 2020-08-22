class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)==0 or len(s)==1 or numRows==1: return s
        row_dict={}
        row_counter=0
        mode=0
        for char in list(s):
            # print(row_counter)
            if row_dict.get(row_counter) is None:
                row_dict[row_counter]=[char]
            else:
                row_dict[row_counter].append(char)
            if mode==0:
                row_counter+=1
                if row_counter>=numRows-1:
                    mode=1
            elif mode==1:
                row_counter-=1
                if row_counter<=0:
                    mode=0
        rearranged=''
        for i in range(numRows):
            if row_dict.get(i) is None:
                break
            rearranged+=''.join(row_dict[i])
        return rearranged
