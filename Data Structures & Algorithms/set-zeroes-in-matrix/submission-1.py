class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        rowZero = False
        colZero = False
        for i in range(0, m):
            if matrix[i][0] == 0:
                rowZero = True
                break
        for j in range(0, n):
            if matrix[0][j] == 0:
                colZero = True
                break
        

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
            elif rowZero:
                matrix[i][0] = 0
        
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
            elif colZero:
                matrix[0][j] = 0
        
        if colZero or rowZero:
            matrix[0][0] = 0



        