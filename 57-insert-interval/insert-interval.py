class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        merged = []
        n = len(intervals)
        i = 0

        # add all intervals to the list that ends before the start of newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        print(f"After Phase 1 - {merged}")
        # merge all the overlapping intervals with the newInterval
        # b_start < a_end
        while i < n and intervals[i][0] <= newInterval[1] and newInterval[0] <= intervals[i][1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            print(f"Updated newInterval - {newInterval}")
            i += 1

        merged.append(newInterval)
        print(f"After Phase 2 - {merged}")

        while i < n:
            merged.append(intervals[i])
            i += 1
        
        print(f"After Phase 3 - {merged}")

        return merged
