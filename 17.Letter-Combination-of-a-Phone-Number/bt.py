class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        n = len(digits)
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def bt(i, cs, partial):
            if i == n:
                cs.append("".join(partial))
                return cs

            for ch in letters[digits[i]]:
                partial.append(ch)
                bt(i + 1, cs, partial)
                partial.pop()

            return cs

        # O(3^n)
        return bt(0, [], [])
