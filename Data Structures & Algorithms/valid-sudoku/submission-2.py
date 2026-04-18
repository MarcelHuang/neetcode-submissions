class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows    = defaultdict(list)
        columns = defaultdict(list)
        squares = defaultdict(list)
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != ".":
                    if num in rows[row] or \
                        num in columns[col] or \
                        num in squares[(row // 3, col // 3)]:
                        return False
                    else:
                        rows[row].append(num)
                        columns[col].append(num)
                        squares[(row // 3, col // 3)].append(num)
        return True
