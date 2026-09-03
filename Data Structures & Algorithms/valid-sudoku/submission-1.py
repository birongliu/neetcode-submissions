class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # key= (cols // 3, rows//3)

        for col in range(len(board)):
            for row in range(len(board)):
                if board[col][row] == ".":
                    continue
                if (board[col][row] in cols[col] or board[col][row] in rows[row]
                    or board[col][row] in squares[(col//3, row//3)]):
                    return False

                cols[col].add(board[col][row])
                rows[row].add(board[col][row])
                squares[(col//3, row//3)].add(board[col][row])

        return True
