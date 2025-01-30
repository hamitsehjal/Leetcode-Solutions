# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        stack = [(root,root.val,root.val)]
        ans = float('-inf')

        while stack:
            node,curMax,curMin = stack.pop()
            curMax = max(curMax,node.val)
            curMin = min(curMin,node.val)

            ans = max(ans,abs(curMax-curMin))

            

            if node.left:
                stack.append((node.left,curMax,curMin))
            if node.right:
                stack.append((node.right,curMax,curMin))
        
        return ans
        