from functools import cache


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        @cache
        def dp(n, target):
            if n == 0:
                return int(target == 0)

            add = dp(n - 1, target + nums[n - 1])
            sub = dp(n - 1, target - nums[n - 1])
            return add + sub

        # O(n * target)
        return dp(len(nums), target)
