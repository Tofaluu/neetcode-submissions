class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        currentStart = newInterval[0]
        currentEnd = newInterval[1]
        length = len(intervals)
        while i < length:
            if newInterval[0] <= intervals[i][1]:
                index = i
                while (i < length and newInterval[1] >= intervals[i][0]):
                    newInterval[1] = max(newInterval[1], intervals[i][1])
                    newInterval[0] = min(newInterval[0], intervals[i][0])
                    i += 1
                intervals = intervals[:index] + [newInterval] + intervals[i:]
                return intervals
            i += 1
        return intervals + [newInterval]