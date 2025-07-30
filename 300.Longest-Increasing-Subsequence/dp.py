class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)

        # O(n)
        dp = [0] * n
        longest = 0

        # O(n^2)
        for i in range(n):
            # O(n)
            dp[i] = 1 + max((dp[j] for j in range(i) if nums[j] < nums[i]), default=0)
            longest = max(longest, dp[i])

        return longest
