# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node,maxSoFar):
            nonlocal count
            
            if not node:
                return
            
            if node.val >= maxSoFar:
                count += 1
                
            maxSoFar = max(maxSoFar,node.val)
            dfs(node.left,maxSoFar)
            dfs(node.right,maxSoFar)
        
        count = 0 
        dfs(root,float('-inf'))
        
        return count