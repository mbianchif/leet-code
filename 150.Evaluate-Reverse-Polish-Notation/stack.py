class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        # O(n)
        stack = []
        for token in tokens:
            if op := ops.get(token):
                b = stack.pop()
                a = stack.pop()
                stack.append(op(a, b))
            else:
                stack.append(int(token))

        return stack.pop()
