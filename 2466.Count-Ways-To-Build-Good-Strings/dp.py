class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7

        # O(high)
        dp = [1] + [0] * high

        # O(high)
        for i in range(1, high + 1):
            dp[i] = ((dp[i - zero] or 0) + (dp[i - one] or 0)) % mod

        # O(high)
        return sum(dp[i] for i in range(low, high + 1)) % mod
