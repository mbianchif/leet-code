class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max_prod = min_prod = nums[0]
        n = len(nums)

        # O(n)
        for i in range(1, n):
            curr_max, curr_min = max_prod * nums[i], min_prod * nums[i]
            max_prod = max(nums[i], curr_max, curr_min)
            min_prod = min(nums[i], curr_max, curr_min)
            res = max(res, max_prod)

        return res
