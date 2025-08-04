from heapq import heappush, heappop


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        visited = set()
        q = [(0, 0)]
        total = 0

        # O(n^2 * logn)
        while q:
            weight, v = heappop(q)
            if v not in visited:
                visited.add(v)
                total += weight

                if len(visited) == n:
                    return total

                x1, y1 = points[v]
                for w in range(n):
                    if w not in visited:
                        x2, y2 = points[w]
                        weight = abs(x1 - x2) + abs(y1 - y2)
                        heappush(q, (weight, w))

        return 0
