class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [1] + [0] * amount

        # O(n * amount)
        for c in coins:
            for j in range(c, amount + 1):
                dp[j] += dp[j - c]

        return dp[amount]
