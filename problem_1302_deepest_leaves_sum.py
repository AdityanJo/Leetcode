# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return root.val
        children=[root.left,root.right]
        children=[child for child in children if child is not None]
        while True:
            children=self.checkChildren(children)
            if type(children) is not list:
                return children

    def checkChildren(self, nodes):
        children=[]
        for node in nodes:
            if node.left is not None:
                children.append(node.left)
            if node.right is not None:
                children.append(node.right)
        if len(children)==0:
            return sum([node.val for node in nodes])
        return children
