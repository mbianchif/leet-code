class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        n = len(arr)
        min_diff = 1 << 31
        values = []

        # O(n^2)
        for i in range(n):
            for j in range(i + 1, n):
                a = min(arr[i], arr[j])
                b = max(arr[i], arr[j])
                diff = b - a

                if diff == min_diff:
                    values.append([a, b])
                elif diff < min_diff:
                    min_diff = diff
                    values = [[a, b]]

        values.sort()
        return values
