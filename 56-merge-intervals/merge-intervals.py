class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals,key=lambda x: x[0])

        merged = []

        for interval in sorted_intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                # conflict - current interval's timestamp is overlapping with previous one
                merged[-1] = [merged[-1][0],max(merged[-1][1],interval[1])]

        return merged