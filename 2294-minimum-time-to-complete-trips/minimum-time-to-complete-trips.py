class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 1, min(time) * totalTrips

        while l < r:
            mid = l + (r - l) // 2

            if self.isPossibleToCompleteTrip(time, totalTrips, mid):
                r = mid

            else:
                l = mid + 1

        return l

    def isPossibleToCompleteTrip(
        self, time: List[int], totalTrips: int, atTime: int
    ) -> bool:
        count = 0
        for time in time:
            count += math.floor(atTime / time)
            if count >= totalTrips:
                return True

        return False
