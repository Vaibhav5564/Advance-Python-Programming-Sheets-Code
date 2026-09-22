def print_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])


def winner(board, player):
    win = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for line in win:
        if all(board[i] == player for i in line):
            return True

    return False


def minimax(board, maximizing):
    if winner(board, "O"):
        return 1

    if winner(board, "X"):
        return -1

    if " " not in board:
        return 0

    if maximizing:
        best = -999

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best = max(best, score)

        return best

    else:
        best = 999

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best = min(best, score)

        return best


def computer_move(board):
    best_score = -999
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"


# Main game
board = [" "] * 9

print("Positions:")
print("0 | 1 | 2")
print("--+---+--")
print("3 | 4 | 5")
print("--+---+--")
print("6 | 7 | 8")

while True:
    print("\nCurrent Board:")
    print_board(board)

    # Human move
    move = int(input("Enter your position (0-8): "))

    if board[move] != " ":
        print("Position already occupied!")
        continue

    board[move] = "X"

    if winner(board, "X"):
        print_board(board)
        print("You Win!")
        break

    if " " not in board:
        print_board(board)
        print("Draw!")
        break

    # Computer move
    computer_move(board)

    if winner(board, "O"):
        print_board(board)
        print("Computer Wins!")
        break