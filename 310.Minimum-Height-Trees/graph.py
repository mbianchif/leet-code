from collections import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        # O(n)
        g = [set() for _ in range(n)]

        # O(m)
        for v, w in edges:
            g[v].add(w)
            g[w].add(v)

        # O(n)
        leaves = deque((v for v, adjs in enumerate(g) if len(adjs) <= 1))
        remaining = n

        # O(n + m)
        while remaining > 2:
            size = len(leaves)

            for _ in range(size):
                v = leaves.popleft()

                for w in g[v]:
                    g[w].remove(v)

                    if len(g[w]) == 1:
                        leaves.append(w)

            remaining -= size

        return list(leaves)
