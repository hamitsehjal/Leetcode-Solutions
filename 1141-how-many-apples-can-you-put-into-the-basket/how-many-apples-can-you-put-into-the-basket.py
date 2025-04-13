class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        carry = 5000

        for i, w in enumerate(weight):
            if w <= carry:
                carry -= w
            else:
                i -= 1
                break

        return i + 1
