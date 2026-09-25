class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int boardLength = 9;

        // Row checker
        for (int row = 0; row < boardLength; ++row) {
            vector<int> currentRowNums;
            for (int col = 0; col < boardLength; ++col) {
                if ('1' <= board[row][col] && board[row][col] <= '9') {
                    if (isInside(board[row][col], currentRowNums)) {
                        return false;
                    }
                    currentRowNums.emplace_back(board[row][col]);
                }
            }
        }

        // Column checker
        for (int col = 0; col < boardLength; ++col) {
            vector<int> currentColNums;
            for (int row = 0; row < boardLength; ++row) {
                if ('1' <= board[row][col] && board[row][col] <= '9') {
                    if (isInside(board[row][col], currentColNums)) {
                        return false;
                    }
                    currentColNums.emplace_back(board[row][col]);
                }
            }
        }

        // Box checker
        for (int row = 0; row < boardLength; row += 3) {
            for (int col = 0; col < boardLength; col += 3) {
                if (!boxChecker(row, col, board)) {
                    return false;
                }
            }
        }

        return true;
    }

    bool isInside(int currentNum, vector<int> nums) {
        for (auto num : nums) {
            if (currentNum == num) {
                return true;
            }
        }

        return false;
    }

    bool boxChecker(int topLeftRow, int topLeftCol, vector<vector<char>>& board) {
        vector<int> currentBoxNums;
        for (int row = topLeftRow; row < topLeftRow + 3; ++row) {
            for (int col = topLeftCol; col < topLeftCol + 3; ++col) {
                if ('1' <= board[row][col] && board[row][col] <= '9') {
                    if (isInside(board[row][col], currentBoxNums)) {
                        return false;
                    }
                    currentBoxNums.emplace_back(board[row][col]);
                }
            }
        }

        return true;
    }
};
