class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        n = len(intervals)

        if n == 0:
            return []

        # O(nlogn)
        intervals.sort(key=lambda v: v[0])

        res = [intervals[0]]

        # O(n)
        for i in range(1, n):
            a, b = intervals[i]
            if res[-1][1] >= a:
                res[-1][1] = max(res[-1][1], b)
            else:
                res.append(intervals[i])

        return res
