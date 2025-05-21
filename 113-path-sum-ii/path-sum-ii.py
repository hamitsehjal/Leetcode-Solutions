# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def dfs(node, curSum, cur):
            if not node:
                return

            curSum += node.val
            cur.append(node.val)

            if not node.left and not node.right:
                # leaf node
                if targetSum == curSum:
                    ans.append(cur[:])
            else:
                # keep exploring
                dfs(node.left, curSum, cur)
                dfs(node.right, curSum, cur)

            cur.pop()

        if not root:
            return []

        ans = []
        dfs(root, 0, [])
        return ans
