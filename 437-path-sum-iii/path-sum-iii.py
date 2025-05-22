# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        def countPaths(node, curSum):
            """Count Paths starting at a specific node"""
            if not node:
                return 0

            curSum += node.val
            ans = 0
            if targetSum == curSum:
                ans = 1

            ans += countPaths(node.left, curSum)
            ans += countPaths(node.right, curSum)

            return ans

        if not root:
            return 0

        """Visit each node exactly once as a starting point"""
        return (
            countPaths(root, 0)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )
