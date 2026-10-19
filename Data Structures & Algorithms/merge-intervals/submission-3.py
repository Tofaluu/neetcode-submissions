class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        newIntervals = []
        length = len(intervals)
        intervals.sort(key=lambda x: x[0])
        i = 0
        while i < length:
            currentI = i
            currentStart = intervals[i][0]
            currentEnd = intervals[i][1]
            while i < length - 1 and currentEnd >= intervals[i + 1][0]:
                currentEnd = max(intervals[i + 1][1], currentEnd)
                i += 1
            newIntervals.append([currentStart, currentEnd])
            i += 1
            
            
        return newIntervals
