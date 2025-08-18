class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        [[1,100],[11,22],[1,11],[2,12]]
        [[1,100],[1,11],[2,12],[11,22]] - sorted by start time
            - 3 removals
        [[1,11],[2,12],[11,22],[1,100]] - sorted by end time

        """
        removals = 0
        intervals.sort(key=lambda x:x[0])
        merged = []

        for interval in intervals:
            
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                # found conflict
                removals += 1
                cur_end_time = interval[1]
                prev_end_time = merged[-1][1]

                merged[-1][1] = max(prev_end_time,cur_end_time)

        
        return merged
        