class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="" or haystack==needle:
            return 0
        else:
            for i in range(len(haystack)-len(needle)+1):
                # print(haystack[i:i+len(needle)])
                if haystack[i:i+len(needle)]==needle:
                    return i
        return -1
