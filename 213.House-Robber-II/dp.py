class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def dp(a, b):
            prev, curr = 0, nums[a]

            # O(n)
            for i in range(a + 2, b + 1):
                curr, prev = max(curr, prev + nums[i - 1]), curr

            return curr

        # O(n)
        return max(dp(1, n), dp(0, n - 1))
