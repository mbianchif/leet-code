class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        nparenthesis = 2 * n

        def bt(solutions, acc, opened):
            if len(acc) == nparenthesis:
                solutions.append("".join(acc))
                return solutions

            if opened < n:
                acc.append("(")
                bt(solutions, acc, opened + 1)
                acc.pop()

            if len(acc) < 2 * opened:
                acc.append(")")
                bt(solutions, acc, opened)
                acc.pop()

            return solutions

        return bt([], [], 0)
