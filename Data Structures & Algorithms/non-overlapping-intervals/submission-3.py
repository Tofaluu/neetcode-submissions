class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        i = 0
        count = 0
        length = len(intervals)
        intervals.sort(key=lambda x : x[0])
        while i < length - 1:
            currentStart = intervals[i][0]
            currentEnd = intervals[i][1]
            if intervals[i][1] > intervals[i + 1][0]:
                count += 1
                currentEnd = min(currentEnd, intervals[i + 1][1])
                i += 1
                while (i < length - 1 and currentEnd > intervals[i + 1][0]):
                    currentEnd = min(currentEnd, intervals[i + 1][1])
                    count += 1
                    i += 1
            i += 1
        return count


