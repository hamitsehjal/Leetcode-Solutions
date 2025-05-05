# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        Preprocess the binary-tree to create a graph

        Perform bfs starting from target node for exactly k steps
        """

        def dfs(node):
            if not node:
                return

            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)

            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)

            dfs(node.left)
            dfs(node.right)

        graph = collections.defaultdict(list)
        dfs(root)

        queue = collections.deque([(target.val, 0)])
        seen = set([target.val])
        ans = []

        while queue:
            node, steps = queue.popleft()
            if steps == k:
                ans.append(node)

            for nei in graph[node]:
                if nei not in seen and steps <= k:
                    seen.add(nei)
                    queue.append((nei, steps + 1))

        print(ans)
        return ans
