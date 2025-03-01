class Solution:
    def arrangeCoins(self, n: int) -> int:
        i,count = 1,0
        while n >= 0:
            n = n - i
            if n >= 0:
                count += 1
            i += 1
        
        print(count)
        return count


        