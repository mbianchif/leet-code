from collections import Counter
from bisect import bisect_left


class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        # O(n)
        counts = Counter(power)
        m = len(counts)

        # O(mlogm)
        power = sorted(counts.keys())

        # O(m)
        dp = [0] * m

        # (mlogm)
        for i, p in enumerate(power):
            j = bisect_left(power, p - 2) - 1
            dp[i] = max(dp[i - 1], counts[p] * p + dp[j])

        # O(m)
        return max(dp)
