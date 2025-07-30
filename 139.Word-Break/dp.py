class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)

        # O(n)
        dp = [False] * n + [True]

        # O(n * m * sum(k))
        for i in range(n - 1, -1, -1):
            for w in wordDict:
                k = len(w)

                # O(k)
                if i + k <= n and s[i : i + k] == w and dp[i + k]:
                    dp[i] = True
                    break

        return dp[0]
