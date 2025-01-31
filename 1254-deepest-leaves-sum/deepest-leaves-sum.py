# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])
        ans = 0

        while queue:
            cur_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()

                if not node:
                    continue
                
                if node.left == None and node.right == None:
                    # leaf node
                    cur_sum += node.val
                    continue

                queue.append(node.left)
                queue.append(node.right)
            
            ans = cur_sum
        
        return ans
        