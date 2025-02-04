# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node: TreeNode | None, curMax: int):
            if not node:
                return 0

            ans = 0
            if node.val >= curMax:
                ans += 1

            curMax = max(curMax, node.val)
            left = dfs(node.left, curMax)
            right = dfs(node.right, curMax)

            return left + right + ans
        
        return dfs(root,float('-inf'))
