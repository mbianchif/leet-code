def is_in_range(i, j, n, m):
    return i >= 0 and j >= 0 and i < n and j < m


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def clear(i, j):
            if not is_in_range(i, j, n, m):
                return

            if grid[i][j] == "1":
                grid[i][j] = 0
                clear(i - 1, j)
                clear(i + 1, j)
                clear(i, j - 1)
                clear(i, j + 1)

        islands = 0

        # O(n * m)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    clear(i, j)
                    islands += 1

        return islands
