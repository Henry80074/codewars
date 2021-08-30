
def valid_solution(board):
    comp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    row_count = 0
    for row in board:
        if sorted(row) == comp:
            row_count += 1

    item = [item for items in board for item in items]

    col_count = 0

    for i in range(9):
        new = item[i::9]
        if sorted(new) == comp:
            col_count += 1

    grid_count = 0
    blocks = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            blocks.append(board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3])

    for i in blocks:
        if sorted(i) == comp:
            grid_count += 1

    if grid_count and row_count and col_count == 9:
        return True
    else:
        return False
