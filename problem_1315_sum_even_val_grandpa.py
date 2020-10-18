# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.even_grandchilds=[]
        self.checkChildren(root, [None, None])
        return sum(self.even_grandchilds)
    def checkChildren(self, node, ancestors):
        if node is not None:
            self.checkChildren(node.left,[ancestors[-1],node.val])
            self.checkChildren(node.right,[ancestors[-1],node.val])
            if ancestors[-2] is not None:
                if ancestors[-2]%2==0:
                    self.even_grandchilds.append(node.val)
            
