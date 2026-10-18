class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for layer in range(n // 2):
            for i in range(layer, n - 1 - layer):
                up = matrix[layer][i]
                right = matrix[i][n - 1 - layer]
                down = matrix[n - 1 - layer][n - 1 - i]
                left = matrix[n - 1 - i][layer]

                matrix[layer][i] = left
                matrix[i][n - 1 - layer] = up
                matrix[n - 1 - layer][n - 1 - i] = right
                matrix[n - 1 - i][layer] = down



