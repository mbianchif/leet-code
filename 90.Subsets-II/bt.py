class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)

        # O(nlogn)
        nums.sort()

        def bt(i, ss, partial):
            if i == n:
                ss.append(partial.copy())
                return ss

            partial.append(nums[i])
            bt(i + 1, ss, partial)
            partial.pop()

            # O(n)
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1

            return bt(i + 1, ss, partial)

        # O(2^n)
        return bt(0, [], [])
