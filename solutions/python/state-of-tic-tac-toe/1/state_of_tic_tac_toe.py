def gamestate(board):
    # Convert board into a mutable list of lists
    board = [list(row) for row in board]

    # Validate dimensions
    if len(board) != 3 or any(len(row) != 3 for row in board):
        raise ValueError("Board must be 3x3")

    # Validate symbols
    if any(cell not in ("X", "O", " ") for row in board for cell in row):
        raise ValueError("Invalid character")

    # Count marks
    x_count = sum(row.count("X") for row in board)
    o_count = sum(row.count("O") for row in board)

    # Check turn order
    if x_count < o_count:
        raise ValueError("Wrong turn order: O started")

    if x_count > o_count + 1:
        raise ValueError("Wrong turn order: X went twice")

    # Get all rows, columns and diagonals
    def get_lines():
        return (
            board +
            [[board[i][j] for i in range(3)] for j in range(3)] +
            [[board[i][i] for i in range(3)]] +
            [[board[i][2 - i] for i in range(3)]]
        )

    # Check winners
    x_win = any(line == ["X"] * 3 for line in get_lines())
    o_win = any(line == ["O"] * 3 for line in get_lines())

    error = "Impossible board: game should have ended after the game was won"

    # Both players cannot win
    if x_win and o_win:
        raise ValueError(error)

    # Validate whether the winner could have won on their last move
    winner = "X" if x_win else "O" if o_win else None

    if winner:
        valid_last_move = False

        for i in range(3):
            for j in range(3):
                if board[i][j] == winner:
                    board[i][j] = " "

                    still_winning = any(
                        line == [winner] * 3 for line in get_lines()
                    )

                    board[i][j] = winner

                    if not still_winning:
                        valid_last_move = True
                        break

            if valid_last_move:
                break

        if not valid_last_move:
            raise ValueError(error)

        # Validate winner's turn
        if winner == "X" and x_count != o_count + 1:
            raise ValueError(error)

        if winner == "O" and x_count != o_count:
            raise ValueError(error)

        return "win"

    # Check draw
    if x_count + o_count == 9:
        return "draw"

    # Otherwise game is ongoing
    return "ongoing"