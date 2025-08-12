from functools import cache


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dxs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def adjacents(i, j):
            for di, dj in dxs:
                ai, aj = i + di, j + dj
                if 0 <= ai < n and 0 <= aj < m:
                    yield ai, aj

        @cache
        def dp(i, j):
            longest_path = 0
            for ai, aj in adjacents(i, j):
                if matrix[i][j] < matrix[ai][aj]:
                    longest_path = max(longest_path, dp(ai, aj))

            return 1 + longest_path

        # O(n * m)
        return max(dp(i, j) for i in range(n) for j in range(m))
