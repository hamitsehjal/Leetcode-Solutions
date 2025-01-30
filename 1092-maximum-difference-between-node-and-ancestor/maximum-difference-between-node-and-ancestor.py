# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        ans = float('-inf')
        def dfs(node,maxVal,minVal):
            
            nonlocal ans
            if not node:
                return
            ans = max(ans,abs(node.val - maxVal))
            ans = max(ans,abs(node.val - minVal))
            
            maxVal = max(maxVal,node.val)
            minVal = min(minVal,node.val)
            dfs(node.left,maxVal,minVal)
            dfs(node.right,maxVal,minVal)

        dfs(root,root.val,root.val)
        return ans
