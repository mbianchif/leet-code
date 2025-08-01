class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        buy1, sell1, buy2 = 0, 0, 0

        # O(n)
        for i in range(n - 1, -1, -1):
            buy = max(sell1 - prices[i], buy1)
            sell = max(buy2 + prices[i], sell1)
            buy1, sell1, buy2 = buy, sell, buy1

        return buy1
