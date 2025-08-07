class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        n = len(intervals)

        # O(nlogn)
        intervals.sort(key=lambda x: x.start)

        # O(n)
        for i in range(1, n):
            if intervals[i - 1].end > intervals[i].start:
                return False

        return True
