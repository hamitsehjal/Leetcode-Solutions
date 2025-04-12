class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:

        projects = sorted(zip(capital,profits))
        i = 0
        heap = []

        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(heap,-projects[i][1])
                i += 1
            
            if len(heap) == 0:
                return w
                
            w -= heapq.heappop(heap)
            
        return w