# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums)==0:
            return None
        max_el=nums.index(max(nums))
        root=TreeNode(val=nums[max_el])
        root.left=self.constructMaximumBinaryTree(nums[:max_el])
        root.right=self.constructMaximumBinaryTree(nums[max_el+1:])
        return root
