# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def countPath(node, target):
            if not node:
                return 0

            count = 0
            if node.val == target:
                count = 1

            count += countPath(node.left, target - node.val)
            count += countPath(node.right, target - node.val)

            return count

        if not root:
            return 0

        return (
            countPath(root, targetSum)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )
