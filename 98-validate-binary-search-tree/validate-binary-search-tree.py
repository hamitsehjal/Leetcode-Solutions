# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        stack = [(root,float('-inf'),float('inf'))]
        while stack:
            node,low,high = stack.pop()
            if not (low < node.val < high):
                return False
            if node.left:
                stack.append((node.left,low,node.val))
            if node.right:
                stack.append((node.right,node.val,high))
        
        return True

        