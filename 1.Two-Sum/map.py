class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        # O(n)
        for i, x in enumerate(nums):
            if (j := seen.get(target - x)) is not None:
                return [i, j]

            seen[x] = i

        return []
