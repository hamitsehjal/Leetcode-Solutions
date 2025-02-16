# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.maxDiameter = 0

        self.maxDepth(root)

        return self.maxDiameter



    def maxDepth(self,root: TreeNode|None)->int:
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        self.maxDiameter = max(self.maxDiameter,left+right)

        return 1 + max(left,right)
        
