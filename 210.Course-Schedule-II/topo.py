from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # O(v)
        graph = [[] for _ in range(numCourses)]
        indegs = [0] * numCourses

        # O(e)
        for w, v in prerequisites:
            graph[v].append(w)
            indegs[w] += 1

        # O(v)
        starters = [v for v, d in enumerate(indegs) if d == 0]
        queue = deque(starters)

        topo = []

        # O(v + e)
        while queue:
            v = queue.popleft()
            topo.append(v)
            for w in graph[v]:
                indegs[w] -= 1
                if indegs[w] == 0:
                    queue.append(w)

        return topo if len(topo) == numCourses else []
