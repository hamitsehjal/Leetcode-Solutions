class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        1. Find the number of non-overlapping intervals
        2. Subtract that from total to find the answer
        """
        if not intervals:
            return 0
        sorted_intervals = sorted(intervals,key = lambda x: x[1])
        count = 1
        end = sorted_intervals[0][1]

        for i in range(1,len(sorted_intervals)):
            if sorted_intervals[i][0] >= end:
                end = sorted_intervals[i][1]
                count += 1

        return len(intervals)-count