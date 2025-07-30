class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        # O(n)
        s = sum(nums)

        if s % 2 != 0:
            return False

        w = s >> 1

        # O(w)
        dp = [True] + [False] * w

        # O(n * w)
        for x in nums:
            for i in range(w, x - 1, -1):
                dp[i] |= dp[i - x]

        return dp[w]
