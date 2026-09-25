class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_length = 9
        row_hash = {i: set() for i in range(board_length)}
        column_hash = {j: set() for j in range(board_length)}
        box_hash = {k: set() for k in range(board_length)}
        box = 0
        for i in range(board_length):
            if i == 3: box = 3
            if i == 6: box = 6
            for j in range(board_length):
                current_box = box
                if j >= 6:
                    current_box = box + 2
                elif j >= 3:
                    current_box = box + 1
                if board[i][j] == ".":
                    continue
                if board[i][j] in row_hash[i]:
                    return False
                if board[i][j] in column_hash[j]:
                    return False
                if board[i][j] in box_hash[current_box]:
                    return False
                row_hash[i].add(board[i][j])
                column_hash[j].add(board[i][j])
                box_hash[current_box].add(board[i][j])
        return True