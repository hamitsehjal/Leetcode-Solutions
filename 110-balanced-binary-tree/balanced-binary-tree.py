# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return (0, True)  # (depth,isBalanced)

            left_depth, left_is_balanced = dfs(node.left)
            right_depth, right_is_balanced = dfs(node.right)

            balance_status = (
                abs(left_depth - right_depth) <= 1
                and left_is_balanced
                and right_is_balanced
            )

            return (1 + max(left_depth, right_depth), balance_status)

        _, status = dfs(root)
        return status
