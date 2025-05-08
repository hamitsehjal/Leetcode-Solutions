# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0
        queue = collections.deque([root])  

        while queue:
            cur_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                cur_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            ans = cur_sum

        return ans
