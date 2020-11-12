# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        curr=[root]
        master_list=[]
        order=True
        while curr:
            if order:
                master_list.append([node.val for node in curr if node])
            else:
                master_list.append([node.val for node in curr if node][::-1])
            order = not order
            curr = [child for node in curr for child in (node.left, node.right) if child]
        return master_list

                
