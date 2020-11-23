class Solution:
    def romanToInt(self, s: str) -> int:
        val=0
        i=len(s)-1
        while i>=0:
            # print(s[i], i, val)
            if i==0:
                if s[i]=='I':
                    val+=1
                elif s[i]=='V':
                    val+=5
                elif s[i]=='X':
                    val+=10
                elif s[i]=='L':
                    val+=50
                elif s[i]=='C':
                    val+=100
                elif s[i]=='D':
                    val+=500
                elif s[i]=='M':
                    val+=1000
                break
            if s[i]=='X' and s[i-1]=='I':
                val+=9
                i-=2
                continue
            elif s[i]=='V' and s[i-1]=='I':
                val+=4
                i-=2
                continue
            elif s[i]=='I':
                val+=1
                i-=1
                continue
            elif s[i]=='V':
                val+=5
                i-=1
                continue
            elif s[i]=='X':
                val+=10
                i-=1
                continue

            if s[i]=='L' and s[i-1]=='X':
                val+=40
                i-=2
                continue
            elif s[i]=='C' and s[i-1]=='X':
                val+=90
                i-=2
                continue
            elif s[i]=='L':
                val+=50
                i-=1
                continue
            elif s[i]=='C':
                val+=100
                i-=1
                continue
            elif s[i]=='X':
                val+=10
                i-=1
                continue

            if s[i]=='D' and s[i-1]=='C':
                val+=400
                i-=2
                continue
            elif s[i]=='M' and s[i-1]=='C':
                val+=900
                i-=2
                continue
            elif s[i]=='D':
                val+=500
                i-=1
                continue
            elif s[i]=='M':
                val+=1000
                i-=1
                continue
            elif s[i]=='C':
                val+=100
                i-=1
                continue

        return val
