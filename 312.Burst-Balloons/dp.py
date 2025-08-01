class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        # O(n)
        nums = [1] + nums + [1]
        n = len(nums)

        # O(n^2)
        dp = [[0] * n for _ in range(n)]

        # O(n^3)
        for k in range(2, n):
            for a in range(n - k):
                b = a + k
                ends = nums[a] * nums[b]
                dp[a][b] = max(
                    dp[a][i] + dp[i][b] + nums[i] * ends for i in range(a + 1, b)
                )

        return dp[0][n - 1]
