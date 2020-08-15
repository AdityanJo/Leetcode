class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={
            '(':')',
            '{':'}',
            '[':']'
        }
        for char in list(s):
            # print(stack)
            if len(stack)==0:
                stack.append(char)
                continue
            if stack[-1] in list(pairs.keys()) and char in list(pairs.keys()):
                stack.append(char)
            elif stack[-1] in list(pairs.keys()) and char in list(pairs.values()):
                if pairs[stack[-1]]==char:
                    stack.pop(-1)
                else:
                    return False
            elif stack[-1] in list(pairs.values()) and char in list(pairs.keys()):
                stack.append(char)
        if len(stack)==0:
            return True
        return False
