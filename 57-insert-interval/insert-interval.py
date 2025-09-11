class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Three Step Process
        1. First add all the intervals that ends before newInterval starts
        2. merge all overlapping intervals with newIntervals
        3. Add the newInterval and rest of the remaining intervals
        """

        merged = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1],intervals[i][1])
            i += 1
        
        merged.append(newInterval)

        while i < n:
            merged.append(intervals[i])
            i += 1
    
        return merged