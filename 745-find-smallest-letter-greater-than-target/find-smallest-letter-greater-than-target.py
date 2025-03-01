class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lo, hi = -1, len(letters)

        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2

            if letters[mid] > target:
                hi = mid
            else:
                lo = mid

        return letters[0] if hi == len(letters) else letters[hi]
