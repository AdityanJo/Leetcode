# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.tree1=[]
        self.tree2=[]
        self.checkChildren(root1, self.tree1)
        self.checkChildren(root2, self.tree2)
        pt1=0
        pt2=0
        t1_len=len(self.tree1)
        t2_len=len(self.tree2)
        merged=[]
        while pt1<t1_len and pt2<t2_len:
            if self.tree1[pt1]<=self.tree2[pt2]:
                merged.append(self.tree1[pt1])
                pt1+=1
            else:
                merged.append(self.tree2[pt2])
                pt2+=1
        if pt1<t1_len:
            merged+=self.tree1[pt1:]
        else:
            merged+=self.tree2[pt2:]
        return merged
    def checkChildren(self, root, tree):
        if root is not None:
            self.checkChildren(root.left, tree)
            tree.append(root.val)
            self.checkChildren(root.right, tree)
