# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)
        
        values = []
        dfs(root)

        dif = float('inf')
        ans = float('inf')
        for value in values:
            new_dif = abs(value-target)
            if new_dif < dif:
                dif = new_dif
                ans = value

        
        return ans

        