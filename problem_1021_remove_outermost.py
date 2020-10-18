class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack=[]
        last_closing=-1
        pairs=[]
        S=list(S)
        for idx,char in enumerate(S):
            if len(stack)>1 and char==')':
                stack.pop()
            elif len(stack)==1 and char==')':
                pairs.append((stack.pop(),(')',idx)))
            else:
                stack.append((char,idx))

        for start, end in pairs[::-1]:
            del(S[end[1]])
            del(S[start[1]])
        return ''.join(S)
