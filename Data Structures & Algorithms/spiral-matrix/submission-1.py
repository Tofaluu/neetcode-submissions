class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rotation = 1
        m = len(matrix)
        n = len(matrix[0])
        order = []
        i = 0
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                order.append(matrix[top][i])
            top += 1

            for j in range(top, bottom + 1):
                order.append(matrix[j][right])
            right -= 1

            if top <= bottom:
                for k in range(right, left - 1, -1):
                    order.append(matrix[bottom][k])
                bottom -= 1

            if left <= right:
                for l in range(bottom, top - 1, -1):
                    order.append(matrix[l][left])
                left += 1

        return order

