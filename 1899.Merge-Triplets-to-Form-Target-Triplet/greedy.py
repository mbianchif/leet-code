class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        m = 3
        ts = [False] * m

        # O(n)
        for t in triplets:
            if any(t[i] > target[i] for i in range(m)):
                continue

            for i in range(m):
                if t[i] == target[i]:
                    ts[i] = True

            if all(ts):
                return True

        return False
