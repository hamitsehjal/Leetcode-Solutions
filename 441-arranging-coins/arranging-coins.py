class Solution:
    def arrangeCoins(self, n: int) -> int:
        i,rows = 1,0
        while n >= 0:
            n = n - i
            if n >= 0:
                rows += 1
            i += 1
        
        return rows


        