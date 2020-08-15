class Solution:
    def reverse(self, x: int) -> int:
        n=0
        if x<0:
            x=-x
            sign_flag=True
        elif x==0:
            return x
        else:
            sign_flag=False
        while x>=1:
            digit=int(x%10)
            # print(digit)
            n=n*10+digit
            x=x/10
        if abs(n)>2**31:
            return 0
        if sign_flag==True:
            return -n
        else:
            return n
    def isPalindrome(self, x: int) -> bool:
        rev=self.reverse(x)
        if rev==x and rev>=0:
            return True
        return False
