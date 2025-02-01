# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        if node.val > high:
            # ignore the entire right subtree
            dfs(node.left)
        elif node.val < low:
            # ignore the entire left subtre
            dfs(node.right)
        else:
            # node.val is in range
            add to answer
            dfs(node.left)
            dfs(node.right)
        """

        def dfs(node, low, high):
            if not node:
                return 0

            if low <= node.val <= high:
                return node.val + dfs(node.left, low, high) + dfs(node.right, low, high)
            elif node.val > high:
                return dfs(node.left, low, high)
            elif node.val < low:
                return dfs(node.right, low, high)

        return dfs(root, low, high)
