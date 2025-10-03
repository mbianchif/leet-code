class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)

        # O(n)
        candies = [1] * n

        # O(n)
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                candies[i] = candies[i - 1] + 1

        # O(n)
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # O(n)
        return sum(candies)
