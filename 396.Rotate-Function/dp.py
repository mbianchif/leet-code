class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)

        # O(n)
        nums_sum = sum(nums)
        fk = sum(i * num for i, num in enumerate(nums))
        max_Fk = fk

        # O(n)
        for k in range(1, n):
            fk = fk + nums_sum - n * nums[n - k]
            max_Fk = max(max_Fk, fk)

        return max_Fk
