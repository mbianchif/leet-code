class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)

        def bt(i, cs, partial, partial_sum):
            if partial_sum > target:
                return cs

            if partial_sum == target:
                cs.append(partial.copy())
                return cs

            if i == n:
                return cs

            partial.append(candidates[i])
            bt(i, cs, partial, partial_sum + candidates[i])
            partial.pop()

            return bt(i + 1, cs, partial, partial_sum)

        # O(2^n)
        return bt(0, [], [], 0)
