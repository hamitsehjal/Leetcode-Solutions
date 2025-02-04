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
                return

            nonlocal count
            if node.val >= curMax:
                count += 1

            curMax = max(curMax, node.val)
            dfs(node.left, curMax)
            dfs(node.right, curMax)
        
        count = 0
        dfs(root,float('-inf'))
        return count
