from collections import Counter
from heapq import heapify, heappop


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize > 0:
            return False

        # O(n)
        counts = Counter(hand)
        heapify(hand)

        # O(n * (logn + groupSize))
        while hand:
            # O(logn)
            card = heappop(hand)
            if counts[card] == 0:
                continue

            # O(groupSize)
            for x in range(card, card + groupSize):
                if counts.get(x, 0) == 0:
                    return False

                counts[x] -= 1

        return True
