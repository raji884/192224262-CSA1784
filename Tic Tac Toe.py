board = [' ' for _ in range(9)]
def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()
def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False
def is_draw():
    return ' ' not in board
player = 'X'
while True:
    print_board()
    try:
        move = int(input(f"Player {player}, enter position (1-9): ")) - 1
        if move < 0 or move > 8:
            print("Invalid position! Choose 1-9.")
            continue
        if board[move] != ' ':
            print("Position already occupied!")
            continue
        board[move] = player
        if check_winner(player):
            print_board()
            print(f"Player {player} Wins!")
            break
        if is_draw():
            print_board()
            print("Game Draw!")
            break
        player = 'O' if player == 'X' else 'X'
    except ValueError:
        print("Please enter a valid number.")
