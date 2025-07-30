from math import inf


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        partial, max_sum = 0, -inf

        # O(n)
        for n in nums:
            partial = max(partial, 0) + n
            if partial > max_sum:
                max_sum = partial

        return int(max_sum)
