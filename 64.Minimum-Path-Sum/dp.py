class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])

        # O(n * m)
        dp = [[0] * m for _ in range(n)]

        # O(n)
        for i in range(n):
            dp[i][1] = dp[i - 1][1] + grid[i][0]

        # O(m)
        for j in range(m):
            dp[1][j] = dp[1][j - 1] + grid[0][j]

        # O(n * m)
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[n - 1][m - 1]
