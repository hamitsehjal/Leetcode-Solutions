# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node,curSum):
            if not node:
                return False
            
            if node.left is None and node.right is None:
                return curSum + node.val == targetSum
            
            return dfs(node.left,curSum+node.val) or dfs(node.right,curSum+node.val)
            

        return dfs(root,0)
        