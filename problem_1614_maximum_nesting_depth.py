class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        max_stack_len=0
        for char in list(s):
            if char=='(':
                stack.append(char)
            if char==')' and stack[-1]:
                stack.pop()
            if len(stack)>max_stack_len:
                max_stack_len=len(stack)
        return max_stack_len
