# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def find_path(root: 'TreeNode', target: 'TreeNode'):
            
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
            
            path = []
            dfs(root)
            return path
        
        p_path = find_path(root,p)
        q_path = find_path(root,q)

        lca = None
        for i in range((min(len(p_path),len(q_path)))):
            if p_path[i] != q_path[i]:
                break
            lca = p_path[i]
        
        return lca

        