class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo,hi = 1,n+1

        while lo + 1 < hi:
            mid = (lo + hi) // 2
            coins = (mid/2)*(mid+1)

            if coins <= n:
                lo = mid
            else:
                hi = mid
        
        return lo