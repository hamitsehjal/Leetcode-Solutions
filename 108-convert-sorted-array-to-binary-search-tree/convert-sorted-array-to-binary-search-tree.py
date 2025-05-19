# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(arr):
            if not arr:
                return None

            index = len(arr) // 2
            root = TreeNode(arr[index])
            root.left = dfs(arr[0:index])
            root.right = dfs(arr[index + 1 :])

            return root

        return dfs(nums)
