class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def two_pointers(i, j):
            # O(n)
            while 0 <= i and j < n and s[i] == s[j]:
                i -= 1
                j += 1

            return i + 1, j - 1

        best = 0, 0

        # O(n^2)
        for i in range(n):
            # O(n)
            ao, bo = two_pointers(i, i)
            if best[1] - best[0] < bo - ao:
                best = ao, bo

            # O(n)
            ae, be = two_pointers(i, i + 1)
            if best[1] - best[0] < be - ae:
                best = ae, be

        # O(n)
        return s[best[0] : best[1] + 1]
