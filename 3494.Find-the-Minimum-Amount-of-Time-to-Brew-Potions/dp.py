class Solution:
    def minTime(self, skill: list[int], mana: list[int]) -> int:
        m = len(skill)

        # O(m)
        dp = [0] * (m + 1)

        # O(n * m)
        for mi in mana:
            for j in range(1, m + 1):
                dp[j] = max(dp[j], dp[j - 1]) + mi * skill[j - 1]

            for j in range(m - 1, 0, -1):
                dp[j] = dp[j + 1] - mi * skill[j]

        return dp[m]
