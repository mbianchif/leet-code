from collections import defaultdict, deque


class Solution:
    def findCheapestPrice(
        self, _: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        g = defaultdict(dict)

        # O(e)
        for v, w, weight in flights:
            g[v][w] = weight

        q = deque([(0, 0, src)])
        cost = {src: 0}

        # O(v + e)
        while q:
            stops, vcost, v = q.popleft()

            if stops > k:
                continue

            for w in g[v]:
                wcost = vcost + g[v][w]
                if wcost < cost.get(w, wcost + 1) and stops <= k:
                    cost[w] = wcost
                    q.append((stops + 1, wcost, w))

        return cost.get(dst, -1)
