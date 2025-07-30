class Solution:
    def checkValidString(self, s: str) -> bool:
        min_p, max_p = 0, 0

        # O(n)
        for p in s:
            if p == "(":
                min_p += 1
                max_p += 1
            elif p == ")":
                min_p -= 1
                max_p -= 1
            else:
                min_p -= 1
                max_p += 1

            min_p = max(min_p, 0)
            if max_p < 0:
                return False

        return min_p == 0
