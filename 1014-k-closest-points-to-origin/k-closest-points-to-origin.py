import heapq as hq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for i,point in enumerate(points):
            x,y = point[0],point[1]
            dist = math.sqrt(x**2+y**2)
            hq.heappush(maxHeap,(-dist,i))

            if len(maxHeap) > k:
                hq.heappop(maxHeap)
        
        ans = []
        while maxHeap:
            _,idx = hq.heappop(maxHeap)
            ans.append(points[idx])
        
        return ans

        