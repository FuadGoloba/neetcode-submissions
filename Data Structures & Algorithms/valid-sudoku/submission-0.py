class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}

        for r in range(len(board)):
            for c in range(len(board)):
                value = board[r][c]
                # skip if position is empty
                if value == ".":
                    continue

                square = (r//3, c//3)

                # create a dictionary for each row, cols, square position as keys and the value being a hashset to check for dupes
                rows.setdefault(r, set())
                cols.setdefault(c, set())
                squares.setdefault(square, set())

                # check if 3 conditions are valid
                if (value in rows[r] or 
                value in cols[c] or
                value in squares[square]):
                    return False

                # add new members to the set of each rows, cols, and squares
                rows[r].add(value)
                cols[c].add(value)
                squares[square].add(value)
        return True