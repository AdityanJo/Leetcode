# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        currA = headA
        currB = headB
        visited ={}
        while currA:
            visited[currA]=1
            currA = currA.next
        while currB:
            if visited.get(currB)==1:
                return currB
            else:
                currB = currB.next
        
