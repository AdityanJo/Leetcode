class Solution:
    def defangIPaddr(self, address: str) -> str:
        n=len(address)
        i=n-1
        while i>=0:
            print(address[i])
            if address[i]=='.':
                address=address[:i]+'[.]'+address[i+1:]
                i-=2
            else:
                i-=1
        # return '[.]'.join(address.split('.'))
        return address
