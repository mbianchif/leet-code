class Solution:
    def getRow(self, n: int) -> list[int]:
        # O(n)
        dp = [1] * (n + 1)

        # O(n)
        for i in range(n):
            for j in range(i, 0, -1):
                dp[j] += dp[j - 1]

        return dp
