class Solution:
    def myPow(self, x: float, n: int) -> float:
        def dnc(x, n):
            if n == 0:
                return 1

            if n == 1:
                return x

            sqrt_p = dnc(x, n // 2)
            return sqrt_p * sqrt_p * dnc(x, n % 2)

        # O(logn)
        p = dnc(x, abs(n))
        return p if n >= 0 else 1 / p
