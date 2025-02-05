# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            maxSum = max(
                maxSum,
                node.val,
                node.val + left,
                node.val + right,
                node.val + left + right,
            )

            return max(node.val,node.val+left,node.val+right)

        maxSum = float("-inf")

        dfs(root)

        return maxSum
