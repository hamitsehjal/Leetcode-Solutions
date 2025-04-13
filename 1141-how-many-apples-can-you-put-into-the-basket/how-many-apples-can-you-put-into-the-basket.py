class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        total = 5000
        i = 0
        
        print(weight)
        while i < len(weight) and total > 0:
            if total >= weight[i]:
                total -= weight[i]
                i += 1
            else:
                total = 0

        return i
        