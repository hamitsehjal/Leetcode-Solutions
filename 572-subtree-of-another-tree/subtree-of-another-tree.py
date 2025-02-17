# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot and not root:
            return False

        if not subRoot:
            return True

        stack = [root]

        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                if self.isSame(node, subRoot):
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return False

    def isSame(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        if root.val != subRoot.val:
            return False

        return self.isSame(root.left, subRoot.left) and self.isSame(
            root.right, subRoot.right
        )
