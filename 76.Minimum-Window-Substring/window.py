from math import inf


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)

        counts = {}

        # O(n)
        for i in range(n):
            counts[s[i]] = 0

        # O(m)
        for j in range(m):
            counts[t[j]] = counts.get(t[j], 0) + 1

        l, r, count = 0, 0, m
        best, head = inf, 0

        # O(n)
        while r < n:
            if counts[s[r]] > 0:
                count -= 1

            counts[s[r]] -= 1
            r += 1

            while count == 0:
                if r - l < best:
                    best = r - l
                    head = l

                if counts[s[l]] == 0:
                    count += 1

                counts[s[l]] += 1
                l += 1

        return "" if best == inf else s[head : head + best]
