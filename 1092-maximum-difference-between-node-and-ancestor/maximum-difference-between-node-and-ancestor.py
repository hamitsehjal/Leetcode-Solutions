# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        '''
        Key insight: Given any two nodes on a same root-to-leaf path, they must have required ancestor-child relationship

        So we keep track of what's the max and min value in each root-to-leaf path and compare the diff among all root-to-leaf paths
        '''

        def dfs(node,cur_max,cur_min):
            if not node:
                return 0
            
            cur_max = max(cur_max,node.val)
            cur_min = min(cur_min,node.val)

            if node.left == None and node.right == None:
                return abs(cur_max - cur_min)
            
            left = dfs(node.left,cur_max,cur_min)
            right = dfs(node.right,cur_max,cur_min)

            return max(left,right)

        return dfs(root,root.val,root.val)

        