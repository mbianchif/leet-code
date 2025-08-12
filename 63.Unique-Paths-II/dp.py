EMPTY = 0


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])

        # O(n * m)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0][1] = 1

        # O(n * m)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if obstacleGrid[i - 1][j - 1] == EMPTY:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[n][m]
