class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = {}
        for x, y, w in flights:
            if x not in graph:
                graph[x] = []
            graph[x].append([y, w])

        heap = [(0, 0, src)]  # cost,stops,city
        visited = {}  # map (city,stops) -> cost
        while heap:
            cost, stops, city = heapq.heappop(heap)

            if city == dst:
                return cost

            if stops > k:
                continue

            # if we have visited this city with fewer stops at lower cost, then skip it
            if (city, stops) in visited and visited[(city, stops)] <= cost:
                continue

            visited[(city,stops)] = cost
            
            for pair in graph.get(city, []):
                nei, weight = pair
                updated_cost = cost + weight
                updated_stops = stops + 1

                heapq.heappush(heap, (updated_cost, updated_stops, nei))

        return -1
