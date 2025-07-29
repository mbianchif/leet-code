class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        n = len(grid)
        m = len(grid[0])

        def in_range(i, j):
            return i >= 0 and j >= 0 and i < n and j < m

        def traverse(i, j, count):
            if not in_range(i, j):
                return

            if grid[i][j] < count:
                return

            grid[i][j] = count
            traverse(i - 1, j, count + 1)
            traverse(i + 1, j, count + 1)
            traverse(i, j - 1, count + 1)
            traverse(i, j + 1, count + 1)

        # O(n * m)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    traverse(i, j, 0)
