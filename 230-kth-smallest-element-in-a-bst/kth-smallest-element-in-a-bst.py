# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def dfs(node: TreeNode|None):
            nonlocal res,k

            if not node:
                return
            
            dfs(node.left)
            k -= 1
            if k == 0:
                # found the kth smallest element
                res = node.val
                return
            dfs(node.right)
        
        res = root.val
        dfs(root)
        return res
        