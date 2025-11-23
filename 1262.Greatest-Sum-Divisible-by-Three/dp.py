class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        dp = [0] * 3

        # O(n)
        for x in nums:
            for y in dp.copy():
                z = x + y
                mod = z % 3
                dp[mod] = max(dp[mod], z)

        return dp[0]
