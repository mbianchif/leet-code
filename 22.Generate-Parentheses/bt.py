class Solution:
    def generateParenthesis(self, n) -> list[str]:
        acc = []

        def bt(open, close):
            if len(acc) == n << 1:
                return ["".join(acc)]

            res = []
            if open < n:
                acc.append("(")
                res.extend(bt(open + 1, close))
                acc.pop()

            if close < open:
                acc.append(")")
                res.extend(bt(open, close + 1))
                acc.pop()

            return res

        # O(2^n)
        return bt(0, 0)
