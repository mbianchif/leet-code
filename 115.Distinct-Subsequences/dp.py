class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        if n < m:
            return 0

        # O(m)
        dp = [0] * m + [1]

        # O(n * m)
        for si in reversed(s):
            for j in range(m):
                if si == t[j]:
                    dp[j] += dp[j + 1]

        return dp[0]
