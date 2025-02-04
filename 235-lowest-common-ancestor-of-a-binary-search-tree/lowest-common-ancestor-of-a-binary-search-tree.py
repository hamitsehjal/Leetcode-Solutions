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

        def dfs(root, ancestors):

            if not root:
                return

            ancestors.append(root)
            nodeToAncestors[root] = ancestors

            dfs(root.left, ancestors.copy())
            dfs(root.right, ancestors.copy())

        nodeToAncestors = collections.defaultdict(list)
        dfs(root,[])

        p_ancestors = nodeToAncestors[p]
        q_ancestors = nodeToAncestors[q]

        lca = None
        for i in range(min(len(p_ancestors),len(q_ancestors))):
            if p_ancestors[i] == q_ancestors[i]:
                lca = p_ancestors[i]
        
        return lca
