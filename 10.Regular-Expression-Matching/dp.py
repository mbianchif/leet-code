from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def matches_asterisk(n, m):
            j = m - 1
            return (
                n > 0
                and m > 1
                and p[j] == "*"
                and (matches_equals(n, m - 1) or matches_dot(m - 1))
            )

        def matches_skip_asterisk(m):
            j = m - 1
            return m > 0 and p[j] == "*"

        def matches_equals(n, m):
            i, j = n - 1, m - 1
            return n > 0 and m > 0 and s[i] == p[j]

        def matches_dot(m):
            j = m - 1
            return m > 0 and p[j] == "."

        @cache
        def dp(n, m):
            if n == 0 and m == 0:
                return True

            if matches_asterisk(n, m):
                return dp(n, m - 2) or dp(n - 1, m)

            if matches_skip_asterisk(m):
                return dp(n, m - 2)

            if matches_equals(n, m) or matches_dot(m):
                return dp(n - 1, m - 1)

            return False

        # O(n * m)
        return dp(len(s), len(p))
