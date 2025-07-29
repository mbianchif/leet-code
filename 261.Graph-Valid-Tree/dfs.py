class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        # O(v)
        graph = [set() for _ in range(n)]

        # O(e)
        for v, w in edges:
            graph[v].add(w)

        visited = set()

        def dfs(start):
            path = set()
            stack = [start]
            while stack:
                v = stack.pop()
                visited.add(v)
                path.add(v)
                for w in graph[v]:
                    if w in path:
                        return False

                    stack.append(w)

            return True

        # O(v + e)
        for v in range(n):
            if v not in visited:
                if not dfs(v):
                    return False

        return True
