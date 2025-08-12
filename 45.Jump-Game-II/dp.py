class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)

        # O(n)
        dp = [0] * n

        # O(n^2)
        for i in range(1, n):
            dp[i] = 1 + min(dp[j] for j in range(i - 1, -1, -1) if j + nums[j] >= i)

        return dp[n - 1]
