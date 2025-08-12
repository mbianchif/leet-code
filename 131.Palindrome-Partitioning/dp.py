class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)

        # O(n^2)
        pal = [[False] * n for _ in range(n)]

        # O(n^2)
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                pal[i][j] = s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1])

        # O(n)
        dp = [[] for _ in range(n + 1)]
        dp[n] = [[]]

        # O(n * 2^n)
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if pal[i][j]:
                    sub = s[i : j + 1]
                    for suffix in dp[j + 1]:
                        dp[i].append([sub] + suffix)

        return dp[0]
