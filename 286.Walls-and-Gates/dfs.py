from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        dxs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        n, m = len(grid), len(grid[0])
        inf = 2147483647

        def adjacents(v):
            for di, dj in dxs:
                ai, aj = v[0] + di, v[1] + dj
                if 0 <= ai < n and 0 <= aj < m and grid[ai][aj] == inf:
                    yield ai, aj

        # O(n * m)
        q = deque((i, j) for i in range(n) for j in range(m) if grid[i][j] == 0)

        # O(n * m)
        while q:
            v = q.popleft()

            for w in adjacents(v):
                if grid[w[0]][w[1]] == inf:
                    grid[w[0]][w[1]] = grid[v[0]][v[1]] + 1
                    q.append(w)
