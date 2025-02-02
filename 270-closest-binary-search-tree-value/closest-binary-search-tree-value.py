# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        def dfs(root):
            stack = []
            cur = root

            while stack or cur:
                while cur:
                    stack.append(cur)
                    cur = cur.left
                
                node = stack.pop()
                values.append(node.val)
                cur = node.right
        
        values = []
        dfs(root)

        ans = root.val
        diff = float('inf')

        for value in values:
            if abs(value-target) < diff:
                diff = abs(value-target)
                ans = value
        
        return ans
        