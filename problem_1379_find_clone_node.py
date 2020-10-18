# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if target.val==cloned.val:
            return cloned
        else:
            children=[cloned.left, cloned.right]
            while True:
                children=self.checkChildren([child for child in children if child is not None], target)
                if type(children) is not list:
                    return children

    def checkChildren(self, nodes, target):
        children=[]
        for node in nodes:
            if node is not None:
                if node.val==target.val:
                    return node
                else:
                    if node.left is not None:
                        if node.left.val==target.val:
                            return node.left
                        else:
                            children.append(node.left)
                    if node.right is not None:
                        if node.right.val==target.val:
                            return node.right
                        else:
                            children.append(node.right)
        return children
