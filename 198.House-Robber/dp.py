class Solution:
    def rob(self, nums: list[int]) -> int:
        prev, curr = 0, nums[0]

        # O(n)
        for i in range(1, len(nums)):
            prev, curr = curr, max(prev + nums[i], curr)

        return curr
