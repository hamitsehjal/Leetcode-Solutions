class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]
            
        degrees = {i: 0 for i in range(n)}
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degrees[u] += 1
            degrees[v] += 1

        queue = deque([u for u in degrees if degrees[u] == 1])
        remaining_nodes = n
        while remaining_nodes > 2:
            level_size = len(queue)
            remaining_nodes -= level_size

            for _ in range(level_size):
                node = queue.popleft()

                for nei in graph[node]:
                    degrees[nei] -= 1
                    if degrees[nei] == 1:
                        queue.append(nei)

        return list(queue)
