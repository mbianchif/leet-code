class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        max_score = max_prev = 0

        # O(n)
        for i, x in enumerate(values):
            max_score = max(max_score, max_prev + x - i)
            max_prev = max(max_prev, x + i)

        return max_score
