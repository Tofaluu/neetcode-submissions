"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([x.start for x in intervals])
        ends = sorted([x.end for x in intervals])
        s = 0
        e = 0
        meeting_rooms = 0
        max_meeting = 0
        while s < len(intervals):
            
            while ends[e] <= starts[s]:
                meeting_rooms -= 1
                e += 1
            meeting_rooms += 1

            if meeting_rooms > max_meeting:
                max_meeting = meeting_rooms
            s += 1
            
        return max_meeting



