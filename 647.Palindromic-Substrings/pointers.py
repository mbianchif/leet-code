class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(i, j):
            palindromes = 0

            # O(n)
            while 0 <= i and j < n:
                if s[i] != s[j]:
                    break

                i -= 1
                j += 1
                palindromes += 1

            return palindromes

        count = 0
        n = len(s)

        # O(n^2)
        for i in range(n):
            # O(n)
            count += expand(i, i)
            count += expand(i, i + 1)

        return count
