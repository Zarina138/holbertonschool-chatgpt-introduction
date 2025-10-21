#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * (len(row) * 4 - 1))

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True, row[0]

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True, board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True, board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True, board[0][2]

    return False, None

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0
    max_moves = 3 * 3

    while moves < max_moves:
        print_board(board)
        try:
            row = int(input(f"Enter row (0-2) for player {player}: "))
            col = int(input(f"Enter column (0-2) for player {player}: "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 2.")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Coordinates out of range. Try again.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player
        moves += 1

        winner, w_player = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {w_player} wins!")
            return

        player = "O" if player == "X" else "X"

    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()

