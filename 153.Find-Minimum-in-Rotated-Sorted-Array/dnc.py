class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        mid = len(nums) // 2
        l = self.findMin(nums[:mid])
        r = self.findMin(nums[mid:])
        return min(l, r)
