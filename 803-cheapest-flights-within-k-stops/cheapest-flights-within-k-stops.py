class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        """
        0 -> [(1,1),(5,2)]
        1 -> [(1,2)]
        2 -> [(1,3)]

        pq = [(0,0,0)]

        """

        graph = {u: [] for u in range(n)}
        for u, v, w in flights:
            graph[u].append([w, v])

        pq = [(0, 0, src)]  # cost,stops,node
        costs = [float("inf")] * n
        costs[src] = 0
        visited = {} # mapping (city,stops) -> cost
        
        while pq:
            cur_cost, stops, u = heapq.heappop(pq)
            if u == dst:
                return cur_cost

            # if cur_cost > costs[u]:
            #     continue
            
            if (u,stops) in visited and visited[(u,stops)] <= cur_cost:
                continue

            visited[(u,stops)] = cur_cost
            
            for c, v in graph[u]:

                if stops > k:
                    continue
                heapq.heappush(pq, [cur_cost + c, stops+1, v])

        return -1
