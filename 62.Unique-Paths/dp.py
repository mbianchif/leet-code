class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # O(m)
        dp = [0] * (m + 1)

        dp[1] = 1

        # O(n * m)
        for _ in range(n):
            for i in range(1, m + 1):
                dp[i] += dp[i - 1]

        return dp[m]
