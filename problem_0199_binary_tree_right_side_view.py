# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None: return []
        curr = [root]
        master_list=[]

        while curr:
            master_list.append(curr[-1].val)
            curr=[child for node in curr for child in (node.left,node.right) if child]

        return master_list
