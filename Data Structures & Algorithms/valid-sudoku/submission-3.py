class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use 3 sets to check a number in the row, col, or square
        # 0. Initialize 3 dictionaries of sets: rows, cols, and squares
        # 1. Double loop 9x9
        # 2. skip if not number
        # 3. return false if the number is in any of the 3 dicts
        # 4. add the number to the 3 dictionaries
        # 5. return true if exit the loop
        rows    = collections.defaultdict(set)
        cols    = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (
                    board[row][col] in rows[row] or
                    board[row][col] in cols[col] or
                    board[row][col] in squares[(row // 3, col // 3)]
                ):
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])
        return True