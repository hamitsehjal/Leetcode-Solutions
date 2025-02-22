# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        if root == p or root == q:
            root is the LCA
        if p is in left subtree and q is in right subtree:
            root is the LCA
        if p and q are in same subtree
        """
        if not root:
            return root

        if root.val == p.val or root.val == q.val:
            return root

        if (p.val > root.val and q.val < root.val) or (
            p.val < root.val and q.val > root.val
        ):
            return root

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
