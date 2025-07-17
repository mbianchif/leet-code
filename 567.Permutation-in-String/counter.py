class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if m < n:
            return False

        win = [0] * 26
        s1_freqs = [0] * 26
        ascii_base = ord("a")

        # O(n)
        for i in range(n):
            s1_freqs[ord(s1[i]) - ascii_base] += 1
            win[ord(s2[i]) - ascii_base] += 1

        # O(m)
        for i in range(m - n):
            if win == s1_freqs:
                return True

            win[ord(s2[i]) - ascii_base] -= 1
            win[ord(s2[i + n]) - ascii_base] += 1

        return win == s1_freqs
