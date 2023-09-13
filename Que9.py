def solve_sudoku(board):
    def is_valid_move(row, col, num):
        # Check row
        if num in board[row]:
            return False

        # Check column
        if num in [board[i][col] for i in range(9)]:
            return False

        # Check 3x3 subgrid
        subgrid_row, subgrid_col = row // 3 * 3, col // 3 * 3
        for i in range(subgrid_row, subgrid_row + 3):
            for j in range(subgrid_col, subgrid_col + 3):
                if board[i][j] == num:
                    return False

        return True

   
