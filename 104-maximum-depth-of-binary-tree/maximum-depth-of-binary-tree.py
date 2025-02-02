# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node,depth):
            nonlocal ans

            if not node:
                return

            if node.left is None and node.right is None:
                # leaf node
                ans = max(ans,depth)
                return

            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        
        if not root:
            return 0
        
        ans = 1
        dfs(root,1)
        return ans

        