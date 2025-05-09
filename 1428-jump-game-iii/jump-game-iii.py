class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        graph = collections.defaultdict(list)

        for index, num in enumerate(arr):
            nxt, prev = index + num, index - num
            if 0 <= nxt <= n - 1:
                graph[index].append(nxt)
            if 0 <= prev <= n - 1:
                graph[index].append(prev)

        queue = collections.deque([start])
        visited = set([start])

        while queue:
            node = queue.popleft()
            if arr[node] == 0:
                return True

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

        return False
