# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_path(root, target):
            path = []
            def dfs(node):
                if not node:
                    return False
                path.append(node)
                if node == target:
                    return True
                if dfs(node.left) or dfs(node.right):
                    return True
                path.pop()
                return False
            dfs(root)
            return path
        
        path_p = find_path(root, p)
        path_q = find_path(root, q)
        
        lca = None
        min_len = min(len(path_p), len(path_q))
        for i in range(min_len):
            if path_p[i] == path_q[i]:
                lca = path_p[i]
            else:
                break
        return lca