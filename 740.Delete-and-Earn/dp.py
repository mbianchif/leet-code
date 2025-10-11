from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        # O(n)
        counts = Counter(nums)
        m = len(counts)

        # O(mlogm)
        nums = sorted(counts.keys())

        # O(m)
        dp = [0] * m

        # O(m)
        for i, x in enumerate(nums):
            j = i - int(nums[i - 1] == x - 1) - 1
            dp[i] = max(dp[i - 1], counts[x] * x + dp[j])

        return dp[m - 1]
