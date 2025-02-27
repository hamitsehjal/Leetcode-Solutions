# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            print(f"Low - {lo} | High - {hi} | Mid - {mid}")
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1

        return hi

