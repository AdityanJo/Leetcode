# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None: return False
        visited=[]
        curr = head
        while curr.next:
            if curr not in visited:
                visited.append(curr)
                curr = curr.next
            else:
                return True
        return False
