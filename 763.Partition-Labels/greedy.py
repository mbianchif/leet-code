class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = [0] * 26
        n = len(s)

        # O(n)
        for i in range(n):
            last[ord(s[i]) - ord("a")] = i

        partitions = []
        l, r = 0, 0

        # O(n)
        for i in range(n):
            r = max(r, last[ord(s[i]) - ord("a")])
            if i == r:
                partitions.append(r - l + 1)
                l = i + 1

        return partitions
