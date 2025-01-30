# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(node,ancestors):
            ans = float('-inf')
            if not node:
                return ans

            for ancestor in ancestors:
                ans = max(ans,abs(node.val-ancestor))
            
            ancestors.append(node.val)
            left = dfs(node.left,ancestors.copy())
            right = dfs(node.right,ancestors.copy())

            return max(left,right,ans)
        
        return dfs(root,[])
        