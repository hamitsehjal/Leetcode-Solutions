class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r = 0,n

        while l < r:
            mid = l + (r-l+1) // 2
            coins = mid * (mid + 1)/2

            print(f"Left - {l} || Right - {r} || Mid - {mid} || Coins - {coins}")
            if coins <= n:
                l = mid
            else:
                r = mid - 1
        
        return l