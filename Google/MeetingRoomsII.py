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
        start_times = []
        end_times = []
        for i in intervals:
            start_times.append(i.start)
            end_times.append(i.end)
        start_times.sort()
        end_times.sort()
        num_rooms, available = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start_times[s] < end_times[e]:
                if available == 0:
                    num_rooms += 1
                else:
                    available -= 1
                s += 1
            else:
                available += 1
                e += 1
        return num_rooms


    def minMeetingRooms2(self, intervals):
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


    def minMeetingRooms3(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key=lambda x: x.start)
        meetings = [intervals[0]]
        count = 1
        for i in intervals[1:]:
            meetings = filter(lambda x: x.end > i.start, meetings)
            meetings.append(i)
            count = max(count, len(meetings))
        return count


    def minMeetingRooms4(self, intervals):
        def compare(x, y):
            if x[0] != y[0]:
                return x[0] - y[0]
            else:
                return x[1] - y[1]

        times = []
        times.extend([(x.start, 1) for x in intervals])
        times.extend([(x.end, -1) for x in intervals])
        times.sort(cmp=compare)
        count = 0
        res = 0
        for time in times:
            if time[1] == 1:
                count += 1
            else:
                count -= 1
            res = max(res, count)
        return res