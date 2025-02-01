# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        queue = collections.deque([root])
        ans = []
        reverse = False

        while queue:
            cur = collections.deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if reverse:
                    cur.appendleft(node.val)
                else:
                    cur.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(list(cur))
            reverse = not reverse
            
        return ans