from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        g = defaultdict(set)

        # O(e)
        for v, w in edges:
            g[v].add(w)
            g[w].add(v)

        def build_cycle(start, end, parents):
            cycle = [end]
            while cycle[-1] != start and (parent := parents[cycle[-1]]):
                cycle.append(parent)

            cycle.reverse()
            n = len(cycle)
            edges = set((cycle[i - 1], cycle[i]) for i in range(1, n))
            edges.add((start, end))
            return edges

        def dfs(v, parents):
            for w in g[v]:
                if w not in parents:
                    parents[w] = v
                    if edge := dfs(w, parents):
                        return edge

                elif w != parents[v]:
                    # O(v)
                    cycle = build_cycle(w, v, parents)

                    # O(e)
                    for edge in reversed(edges):
                        v, w = tuple(edge)
                        if (v, w) in cycle or (w, v) in cycle:
                            return edge

                    break

            return []

        # O(v + e)
        return dfs(1, {1: None})
