class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        a, b = 0, cost[0]

        # O(n)
        for i in range(1, len(cost)):
            a, b = b, cost[i] + min(a, b)

        return min(a, b)
