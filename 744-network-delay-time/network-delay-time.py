class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append([v, w])  # neighbour,weight

        distances = {u + 1: float("inf") for u in range(n)}
        distances[k] = 0
        pq = [[0, k]]  # weight,node

        while pq:
            current_weight, node = heapq.heappop(pq)
            if current_weight > distances[node]:
                continue

            for nei, wei in graph[node]:
                weight = current_weight + wei
                if weight < distances[nei]:
                    distances[nei] = weight
                    heapq.heappush(pq, [weight, nei])

        ans = max(distances.values())
        if ans == float("inf"):
            return -1

        return ans
