class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)

        def dfs(i, ss, partial):
            if i == n:
                # O(n)
                ss.append(partial.copy())
                return ss

            partial.append(nums[i])
            dfs(i + 1, ss, partial)
            partial.pop()

            return dfs(i + 1, ss, partial)

        # O(n * 2^n)
        return dfs(0, [], [])
