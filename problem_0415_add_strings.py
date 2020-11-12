class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result=[]
        carry=0
        i = len(num1)-1
        j = len(num2)-1
        while i>=0 or j>=0:
            x1 = ord(num1[i])-ord('0') if i>=0 else 0
            x2 = ord(num2[j])-ord('0') if j>=0 else 0
            x = (x1+x2+carry)%10
            carry = (x1+x2+carry)//10
            # print(x, carry)
            result.append(x)
            i-=1
            j-=1
        if carry!=0:
            result.append(carry)
        return ''.join([str(i) for i in result[::-1]])
