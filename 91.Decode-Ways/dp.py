class Solution:
    def numDecodings(self, s: str) -> int:
        prev1, prev2 = 1, 0

        def could_be_multiple(i):
            if s[i] == "1":
                return True

            if s[i] == "2" and i + 1 < len(s) and int(s[i + 1]) < 7:
                return True

            return False

        # O(n)
        for i in range(len(s) - 1, -1, -1):
            curr = prev1 * (s[i] != "0") + prev2 * could_be_multiple(i)
            prev2, prev1 = prev1, curr

        return prev1
