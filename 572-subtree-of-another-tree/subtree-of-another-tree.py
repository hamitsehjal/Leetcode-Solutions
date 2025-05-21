# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False

        isLeftSame = self.dfs(root.left, subRoot.left)
        isRightSame = self.dfs(root.right, subRoot.right)

        return isLeftSame and isRightSame

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            if node.val == subRoot.val:
                # potential match, check left and right subtree
                if self.dfs(node, subRoot):
                    return True

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False
