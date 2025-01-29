# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        ans = float('-inf')
        def dfs(node,ancestors):
            
            nonlocal ans
            if not node:
                return
            # print(f"node: {node.val} <--> Ancestors: {ancestors}")
            for ancestor in ancestors:
                ans = max(ans,abs(node.val - ancestor))
            
            ancestors.append(node.val)
            dfs(node.left,ancestors.copy())
            dfs(node.right,ancestors.copy())

        dfs(root,[])
        return ans
