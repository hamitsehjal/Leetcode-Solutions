class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:

        insertion_point = self.findInsertionPoint(intervals, newInterval)
        intervals.insert(insertion_point, newInterval)

        return self.mergeIntervals(intervals)

    def findInsertionPoint(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> int:
        left, right = 0, len(intervals) - 1

        while left <= right:
            mid = (left + right) // 2

            if intervals[mid][0] == newInterval[0]:
                return mid
            elif intervals[mid][0] < newInterval[0]:
                left += 1
            else:
                right -= 1

        return left

    def mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][0] = min(interval[0], merged[-1][0])
                merged[-1][1] = max(interval[1], merged[-1][1])

        return merged
