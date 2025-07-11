from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # O(n * m)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1

                elif grid[i][j] == 2:
                    q.append((i, j))

        adjs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def adjacents(v):
            i, j = v
            for di, dj in adjs:
                ai, aj = i + di, j + dj
                if 0 <= ai < n and 0 <= aj < m:
                    yield ai, aj

        time = 0

        # O(n * m)
        while fresh > 0 and q:
            time += 1
            for _ in range(len(q)):
                v = q.popleft()
                for w in adjacents(v):
                    i, j = w
                    if grid[i][j] == 1:
                        grid[i][j] = 2
                        q.append(w)
                        fresh -= 1

        return time if fresh == 0 else -1
