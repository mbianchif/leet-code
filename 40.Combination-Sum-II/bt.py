class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)

        # O(nlogn)
        candidates.sort()

        def bt(i, cs, partial, partial_sum):
            if partial_sum > target:
                return cs

            if partial_sum == target:
                # O(n)
                cs.append(partial.copy())
                return cs

            for j in range(i, n):
                if i < j and candidates[j - 1] == candidates[j]:
                    continue

                partial.append(candidates[j])
                bt(j + 1, cs, partial, partial_sum + candidates[j])
                partial.pop()

            return cs

        # O(n * 2^n)
        return bt(0, [], [], 0)
