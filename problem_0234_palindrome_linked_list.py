# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None: return True
        if head.next is None: return True
        curr = head
        val = []
        while curr:
            # val = val ^ curr.val
            val.append(curr.val)
            curr = curr.next
        # print(val)
        if val == val[::-1]:
            return True
        else:
            return False
