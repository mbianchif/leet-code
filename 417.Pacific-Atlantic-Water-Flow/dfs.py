class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        n, m = len(heights), len(heights[0])
        dxs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def adjacents(i, j):
            for di, dj in dxs:
                ai, aj = i + di, j + dj
                if 0 <= ai < n and 0 <= aj < m:
                    yield ai, aj

        def bfs(s):
            # O(n + m)
            visited = set(s)

            # O(n * m)
            while s:
                i, j = s.pop()

                for ai, aj in adjacents(i, j):
                    if (ai, aj) not in visited and heights[i][j] <= heights[ai][aj]:
                        visited.add((ai, aj))
                        s.append((ai, aj))

            return visited

        p, a = [], []

        # O(n)
        for i in range(n):
            p.append((i, 0))
            a.append((i, m - 1))

        # O(m)
        for j in range(m):
            p.append((0, j))
            a.append((n - 1, j))

        # O(n * m)
        atlantic = bfs(a)
        return [list(x) for x in bfs(p) if x in atlantic]
