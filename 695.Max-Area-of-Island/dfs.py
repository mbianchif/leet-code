class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def in_range(i, j):
            return i >= 0 and j >= 0 and i < n and j < m

        def clear_island(i, j):
            if not in_range(i, j):
                return 0

            if grid[i][j] == 0:
                return 0

            area = 1
            grid[i][j] = 0
            area += clear_island(i - 1, j)
            area += clear_island(i + 1, j)
            area += clear_island(i, j - 1)
            area += clear_island(i, j + 1)
            return area

        max_area = 0

        # O(n * m)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_area = max(max_area, clear_island(i, j))

        return max_area
