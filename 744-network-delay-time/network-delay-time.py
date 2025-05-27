import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))  # weight,vertex

        visited = set()
        minHeap = [(0, k)]

        while minHeap:
            travel_time, node = heapq.heappop(minHeap)
            visited.add(node)

            if len(visited) == n:
                return travel_time

            for time, nei in graph[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (time+travel_time, nei))

        return -1
