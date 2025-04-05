from heapq import heappush,heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        we only want to store k closest one's
        """
        heap = [] # max-heap

        for i,(x,y) in enumerate(points):
            dist = math.sqrt((x*x)+(y*y))
            heappush(heap,(-dist,i))

            if len(heap) > k:
                heappop(heap)
        
        ans = []
        while heap:
            _,i = heappop(heap)
            ans.append(points[i])
        
        return ans
