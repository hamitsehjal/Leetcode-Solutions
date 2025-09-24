class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        closest - min distance 

        for point in points:
            # calculate the distance
            # add (distance, point) to max-heap

            # if len(max-heap) > k:
                pop from max-heap
        """
        max_heap = []

        for point in points:
            x,y = point
            distance = -(math.sqrt((x**2) + (y**2)))
            heapq.heappush(max_heap,(distance,point))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        ans = []
        while max_heap:
            _,point = heapq.heappop(max_heap)
            ans.append(point)
        
        return ans