class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        carry = 5000

        print(weight)
        for i, w in enumerate(weight):
            if w <= carry:
                carry -= w
                print(f"Carrying - {i} | {w} | remaining - {carry}")
            else:
                i -= 1
                break

        return i + 1
