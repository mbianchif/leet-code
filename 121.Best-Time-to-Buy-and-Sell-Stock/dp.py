class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit, min_so_far = 0, prices[0]

        # O(n)
        for i in range(1, len(prices) + 1):
            max_profit = max(max_profit, prices[i - 1] - min_so_far)
            min_so_far = min(min_so_far, prices[i - 1])

        return max_profit
