# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nums = []

        self.inOrderDfs(root)

        return self.nums[k-1]
    
    def inOrderDfs(self,root: TreeNode|None)->list | None:
        if not root:
            return
        
        self.inOrderDfs(root.left)
        self.nums.append(root.val)
        self.inOrderDfs(root.right)


