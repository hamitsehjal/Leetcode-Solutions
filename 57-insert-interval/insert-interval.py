class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """
        Three Step Process
        1. Add all intervals that start before newInterval to the merged list
        2. Merge all overlapping intervals with the new-interval
        3. Add the new-interval and rest of the remaining intervals
        """
        merged = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        merged.append(newInterval)

        while i < n:
            merged.append(intervals[i])
            i += 1

        return merged
