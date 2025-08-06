from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        counts = defaultdict(int)
        l = max_freq = 0

        # O(n)
        for r in range(n):
            counts[s[r]] += 1
            max_freq = max(max_freq, counts[s[r]])

            if (r - l + 1) - max_freq > k:
                counts[s[l]] -= 1
                l += 1

        return n - l
