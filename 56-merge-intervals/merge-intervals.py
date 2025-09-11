class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []

        for i in range(len(intervals)):
            if merged and intervals[i][0] <= merged[-1][1]:
                merged[-1][1] = max(intervals[i][1],merged[-1][1])
            else:
                merged.append(intervals[i])

        return merged