class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        merged = []
        removals = 0

        for interval in sorted_intervals:
            if not merged or interval[0] >= merged[-1][1]:
                merged.append(interval)
            else:
                # conflict
                merged[-1][0] = min(
                    merged[-1][0], interval[0]
                )  # prefer smaller value to minimize future overlapping
                merged[-1][1] = min(
                    merged[-1][1], interval[1]
                )  # prefer smaller value to minimize future overlapping
                removals += 1

        return removals
