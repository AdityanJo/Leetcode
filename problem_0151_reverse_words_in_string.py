class Solution:
    # def reverseWords(self, s: str) -> str:
    #     words=['']
    #     # print(list(s))
    #     for char in list(s):
    #         if char==' ' and words[-1]!='':
    #             words.append('')
    #         elif char==' ' and words[-1]=='':
    #             continue
    #         elif char!='':
    #             words[-1]+=char
    #     if words[-1]=='':
    #         del(words[-1])
    #     # print(words)
    #     return ' '.join(words[::-1])
    def reverseWords(self, s: str) -> str:
        words=s.strip().split(' ')
        words=[word for word in words if word!='']
        return ' '.join(words[::-1])
