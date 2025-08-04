from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        g = defaultdict(list)

        # O(e)
        for v, w in tickets:
            g[v].append(w)

        # O(eloge)
        for v in g:
            g[v].sort(reverse=True)

        s = ["0"]
        itinerary = []

        # O(e)
        while s:
            print(s, itinerary)
            while g[s[-1]]:
                s.append(g[s[-1]].pop())

            itinerary.append(s.pop())

        # O(e)
        itinerary.reverse()
        return itinerary
