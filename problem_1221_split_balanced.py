class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack=[]
        splits=[]
        current_state=0
        state_dict={
            'R':1,
            'L':-1
        }
        for char in list(s):
            stack.append(char)
            current_state+=state_dict[char]
            if current_state==0 and len(stack)!=0:
                splits.append(''.join(stack))
                stack=[]
        return len(splits)
                
