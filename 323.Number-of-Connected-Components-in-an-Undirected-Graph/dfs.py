class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        # O(v)
        g = {v: set() for v in range(n)}

        # O(e)
        for v, w in edges:
            g[v].add(w)
            g[w].add(v)

        visited = set()

        def dfs(start):
            s = [start]
            while s:
                v = s.pop()

                for w in g[v]:
                    if w not in visited:
                        visited.add(w)
                        s.append(w)

        components = 0

        # O(v + e)
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)

        return components
