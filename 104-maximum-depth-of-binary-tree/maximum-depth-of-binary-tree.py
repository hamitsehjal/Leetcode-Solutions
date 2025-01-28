# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([root] if root else [])
        depth = 0

        while queue:
            num_of_nodes_at_current_level = len(queue)
            depth += 1
            for _ in range(num_of_nodes_at_current_level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth
        

            
        