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
                return [0, True]  # (depth,isBalanced)

            l_depth, l_status = dfs(node.left)
            r_depth, r_status = dfs(node.right)

            status = (l_status and r_status) and abs(r_depth-l_depth) <= 1
            depth = 1 + max(l_depth, r_depth)

            return [depth, status]

        return dfs(root)[1]
