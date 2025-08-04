from heapq import heappush, heappop


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dxs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def adjacents(v):
            for di, dj in dxs:
                ai, aj = v[0] + di, v[1] + dj
                if 0 <= ai < n and 0 <= aj < n:
                    yield ai, aj

        start = 0, 0
        dist = {start: grid[0][0]}
        q = [(grid[0][0], start)]

        # O((v + e) * logv)
        while q:
            t, v = heappop(q)
            if v == (n - 1, n - 1):
                return t

            for w in adjacents(v):
                tn = max(t, grid[w[0]][w[1]])
                if tn < dist.get(w, tn + 1):
                    dist[w] = tn
                    heappush(q, (tn, w))

        return -1
