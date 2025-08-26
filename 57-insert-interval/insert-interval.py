class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """
        Approach 1:
        - find the insertion point and insert it
            - binary search based on start time
            - result: [[1,3],[2,5],[6,9]]
        - merge the overlapping intervals
        """
        insertion_point = self.findInsertionPoint(intervals, newInterval)
        intervals.insert(insertion_point, newInterval)

        print(f"Intervals before insertion",intervals)
        return self.mergeOverlappingIntervals(intervals)

    def findInsertionPoint(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> int:
        l, r = 0, len(intervals) - 1

        while l <= r:
            mid = (l + r) // 2
            start_time = intervals[mid][0]
            if start_time == newInterval[0]:
                return mid
            elif start_time < newInterval[0]:
                l += 1
            else:
                r -= 1

        return l

    def mergeOverlappingIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []

        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]

        return merged
