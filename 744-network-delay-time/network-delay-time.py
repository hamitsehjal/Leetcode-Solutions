class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u - 1].append((v - 1, w))

        distances = [inf] * n
        distances[k - 1] = 0
        heap = [[0, k - 1]]  # weight,node

        while heap:
            cur_dist, node = heapq.heappop(heap)
            if cur_dist > distances[node]:
                continue

            for nei, weight in graph[node]:
                dist = cur_dist + weight
                if dist < distances[nei]:
                    distances[nei] = dist
                    heapq.heappush(heap, [dist, nei])

        ans = max(distances)
        return ans if ans < inf else -1
