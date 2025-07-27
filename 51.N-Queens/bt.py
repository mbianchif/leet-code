class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def gen_board(queens):
            # O(n)
            return [j * "." + "Q" + (n - j - 1) * "." for j in queens]

        def validate_queens(queens, cols, added):
            row, col = added

            if cols[col]:
                return False

            # O(n)
            for i, j in enumerate(queens):
                if abs(i - row) == abs(j - col):
                    return False

            return True

        def bt(solutions, queens, cols):
            i = len(queens)

            if i == n:
                solutions.append(gen_board(queens))
                return solutions

            for j in range(n):
                if validate_queens(queens, cols, (i, j)):
                    cols[j] = True
                    queens.append(j)
                    bt(solutions, queens, cols)
                    cols[j] = False
                    queens.pop()

            return solutions

        # O(n! * n)
        return bt([], [], [False] * n)
