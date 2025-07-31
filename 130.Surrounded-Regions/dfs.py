class Solution:
    def solve(self, board: list[list[str]]) -> None:
        n, m = len(board), len(board[0])
        dxs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def adjacents(i, j):
            for di, dj in dxs:
                ai, aj = i + di, j + dj
                if 0 <= ai < n and 0 <= aj < m:
                    yield ai, aj

        def dfs(i, j):
            board[i][j] = "V"
            s = [(i, j)]

            # O(n * m)
            while s:
                i, j = s.pop()

                for ai, aj in adjacents(i, j):
                    if board[ai][aj] == "O":
                        board[ai][aj] = "V"
                        s.append((ai, aj))

        # O(n)
        for i in range(n):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][m - 1] == "O":
                dfs(i, m - 1)

        # O(m)
        for j in range(m):
            if board[0][j] == "O":
                dfs(0, j)
            if board[n - 1][j] == "O":
                dfs(n - 1, j)

        map_table = {
            "O": "X",
            "V": "O",
            "X": "X",
        }

        # O(n * m)
        for i in range(n):
            for j in range(m):
                board[i][j] = map_table[board[i][j]]
