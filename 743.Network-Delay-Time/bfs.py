from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        g = defaultdict(list)

        # O(e)
        for u, v, w in times:
            g[u].append((v, w))

        q = [(0, k)]
        dist = {k: 0}

        # O((v + e) * logv)
        while q:
            udist, u = heappop(q)

            for v, w in g[u]:
                vdist = udist + w
                if vdist < dist.get(v, vdist + 1):
                    dist[v] = vdist
                    heappush(q, (vdist, v))

        # O(v)
        return max(dist.values()) if len(dist) == n else -1
