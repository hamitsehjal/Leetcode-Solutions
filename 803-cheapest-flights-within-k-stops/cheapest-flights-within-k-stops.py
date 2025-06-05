class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k+1):
            temp = dist[:]

            for u,v,w in flights:
                if dist[u] != float('inf'):
                    temp[v] = min(temp[v],dist[u] + w)
            
            dist = temp
        

        if dist[dst] == float('inf'):
            return -1
        
        return dist[dst]
