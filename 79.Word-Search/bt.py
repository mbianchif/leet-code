from typing import Iterable


class Solution:
    def get_inits(self, board, n, m, c) -> Iterable:
        for i in range(n):
            for j in range(m):
                if board[i][j] == c:
                    yield i, j

    def in_bounds(self, n, m, i, j) -> bool:
        return i >= 0 and j >= 0 and i < n and j < m

    def adjacents(self, i, j) -> Iterable:
        yield i, j + 1
        yield i + 1, j
        yield i, j - 1
        yield i - 1, j

    def exist(self, board: list[list[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        def dfs(pos, steps):
            steps.add(pos)

            if len(steps) == len(word):
                return True

            it = filter(lambda x: self.in_bounds(n, m, *x), self.adjacents(*pos))
            it = filter(lambda x: x not in steps, it)
            it = filter(lambda x: board[x[0]][x[1]] == word[len(steps)], it)

            for ady in it:
                if dfs(ady, steps):
                    return True

            steps.remove(pos)
            return False

        # O(n * m)
        asc = list(self.get_inits(board, n, m, word[0]))
        des = list(self.get_inits(board, n, m, word[-1]))

        it = asc
        if len(asc) > len(des):
            # O(k)
            word = word[::-1]
            it = des

        # O(n * m * k)
        for init in it:
            if dfs(init, set()):
                return True

        return False
