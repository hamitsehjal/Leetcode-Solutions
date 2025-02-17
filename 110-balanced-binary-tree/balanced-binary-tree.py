# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        _,status = self.dfs(root)
        return status


        
    def dfs(self,root: TreeNode|None)->tuple[int,bool]:
        if not root:
            return (0,True)
        
        l_height,l_status = self.dfs(root.left)
        r_height,r_status = self.dfs(root.right)

        status = abs(l_height-r_height) <= 1 and l_status and r_status

        return (1+max(l_height,r_height),status)
