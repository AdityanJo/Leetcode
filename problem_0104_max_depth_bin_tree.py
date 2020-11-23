# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        curr=[root]
        i=0
        while curr:
            curr = [child for node in curr for child in (node.left, node.right) if child]
            i+=1
        return i
