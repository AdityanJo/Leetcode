class Solution:
    def countBits(self, num: int) -> List[int]:
        output=[0]
        offset=1
        for i in range(1,num+1):
            if i==offset*2:
                offset*=2
            output.append(output[i-offset]+1)
            # print(i, offset*2, output[i-offset], output)
        return output
