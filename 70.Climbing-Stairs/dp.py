class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1

        # O(n)
        for _ in range(n):
            a, b = b, a + b

        return b
