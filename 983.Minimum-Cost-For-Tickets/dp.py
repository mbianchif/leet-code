class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        n = len(days)

        def find_idx(i, amount):
            for j in range(i + 1, n):
                if days[i] + amount - 1 < days[j]:
                    return j

            return n

        # O(n)
        dp = [0] * (n + 1)

        # O(n^2)
        for i in range(n - 1, -1, -1):
            day = costs[0] + dp[i + 1]
            week = costs[1] + dp[find_idx(i, 7)]
            month = costs[2] + dp[find_idx(i, 30)]
            dp[i] = min(day, week, month)

        return dp[0]
