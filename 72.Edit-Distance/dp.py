class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        # O(m)
        curr = [0] * (m + 1)
        prev = list(range(m + 1))

        # O(n * m)
        for i in range(1, n + 1):
            curr[0] = i

            # O(m)
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])

            curr, prev = prev, curr

        return prev[m]
