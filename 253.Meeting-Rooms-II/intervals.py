from heapq import heappop, heappush


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        n = len(intervals)
        if n == 0:
            return 0

        # O(nlogn)
        intervals.sort(key=lambda x: x.start)

        heap = [intervals[0].end]

        # O(nlogn)
        for i in range(1, n):
            if heap[0] <= intervals[i].start:
                heappop(heap)

            heappush(heap, intervals[i].end)

        return len(heap)
