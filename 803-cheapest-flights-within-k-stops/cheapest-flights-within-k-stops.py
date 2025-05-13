class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for x, y, price in flights:
            graph[x].append([y, price])
        
        # [cost, stops, city]
        heap = [(0, 0, src)]
        # Track best cost for each node at each stop count
        visited = {}
        
        while heap:
            cost, stops, city = heapq.heappop(heap)
            
            # If we reached destination, return cost
            if city == dst:
                return cost
            
            # If we've used too many stops, continue
            if stops > k:
                continue
                
            # Skip if we've seen this city with fewer stops at lower cost
            if (city, stops) in visited and visited[(city, stops)] <= cost:
                continue
                
            visited[(city, stops)] = cost
            
            # Explore neighbors
            for nei, price in graph[city]:
                heapq.heappush(heap, (cost + price, stops + 1, nei))
        
        return -1