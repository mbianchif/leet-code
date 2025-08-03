from collections import Counter
from heapq import heapify, heappop


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # O(n)
        c = Counter(nums)

        # O(n)
        h = [(-count, x) for x, count in c.items()]
        heapify(h)

        # O(k * logn)
        return [heappop(h)[1] for _ in range(k)]
