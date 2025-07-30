from math import inf


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # O(amount)
        dp = [0] + [inf] * amount

        # O(n * amount)
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], 1 + dp[i - c])

        return int(dp[amount]) if dp[amount] < inf else -1
