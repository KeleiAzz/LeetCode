# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        start_times = sorted([i.start for i in intervals])
        end_times = sorted([i.end for i in intervals])
        rooms = 0
        end = 0
        for start in start_times:
            if start < end_times[end]:
                rooms += 1
            else:
                end += 1
        return rooms
