from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        g = defaultdict(dict)

        # O(e)
        for u, v, w in times:
            g[u][v] = w

        q = [(0, k)]
        dist = {k: 0}

        # O((v + e) * logv)
        while q:
            vdist, v = heappop(q)

            for w in g[v]:
                wdist = vdist + g[v][w]
                if wdist < dist.get(w, wdist + 1):
                    dist[w] = wdist
                    heappush(q, (wdist, w))

        # O(v)
        return max(dist.values()) if len(dist) == n else -1
