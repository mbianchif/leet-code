class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)

        def dfs(ps, acc, visited):
            if len(acc) == n:
                # O(n)
                ps.append(acc.copy())
                return ps

            # O(n)
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    acc.append(nums[i])
                    dfs(ps, acc, visited)
                    visited[i] = False
                    acc.pop()

            return ps

        # O(n!)
        return dfs([], [False] * n, [])
