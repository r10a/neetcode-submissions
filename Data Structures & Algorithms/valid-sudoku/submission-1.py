class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            seen_row = set()
            seen_col = set()
            for j in range(len(board)):
                if board[i][j] != ".":
                    if board[i][j] in seen_row:
                        return False
                    else:
                        seen_row.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in seen_col:
                        return False
                    else:
                        seen_col.add(board[j][i])

            seen_block = set()
            block_row = math.floor(i / 3) * 3
            block_col = (i * 3) % 9
            for row in range(block_row, block_row + 3):
                for col in range(block_col, block_col + 3):
                    if board[row][col] != '.':
                        if board[row][col] in seen_block:
                            return False
                        else:
                            seen_block.add(board[row][col])

        return True