class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        startingChars = []
        width = len(board)
        length = len(board[0])
        for i in range(width):
            for j in range(length):
                if board[i][j] == word[0]:
                    startingChars.append((i, j))

        if not startingChars:
            return False

        def recursiveStep(word, pair, currentPairs, board):
            r, c = pair
            if word == "":
                return True
            elif r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[0] or (r, c) in currentPairs:
                return False
            else:
                currentPairs.append((r, c))
                result = recursiveStep(word[1: len(word)], (r - 1, c), currentPairs, board) or recursiveStep(word[1: len(word)], (r + 1, c), currentPairs, board) or recursiveStep(word[1: len(word)], (r, c - 1), currentPairs, board) or recursiveStep(word[1: len(word)], (r, c + 1), currentPairs, board)
                if result:
                    return True
                currentPairs.pop()
                return False

        for (r, c) in startingChars:
            
            if recursiveStep(word, (r, c), [], board):
                return True
        return False





