from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
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

        # O(v + e)
        visited = 0
        while queue:
            v = queue.popleft()
            visited += 1
            for w in graph[v]:
                indegs[w] -= 1
                if indegs[w] == 0:
                    queue.append(w)

        return visited == numCourses
