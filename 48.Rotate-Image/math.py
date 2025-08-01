class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        # O(n)
        for i in range(n // 2):
            j = n - i - 1
            matrix[i], matrix[j] = matrix[j], matrix[i]

        # O(n^2)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
