# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def maxHeight(node):
            '''
            Returns the max height of a tree rooted at node
            '''
            nonlocal max_diameter

            if not node:
                return 0
            
            left = maxHeight(node.left)
            right = maxHeight(node.right)
            max_diameter = max(max_diameter,left+right)
            return 1 + max(left,right)

        max_diameter = float('-inf')
        maxHeight(root)
        return max_diameter
        