board = [' ' for x in range(10)]

def print_board(board):
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("-----------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("-----------")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")

def insert_board(letter, position):
    board[position] = letter

def space_is_free(position):
    return board[position] == ' '

def is_winner(board, letter):
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[1] == letter and board[4] == letter and board[7] == letter) or
    (board[2] == letter and board[5] == letter and board[8] == letter) or
    (board[3] == letter and board[6] == letter and board[9] == letter) or
    (board[1] == letter and board[5] == letter and board[9] == letter) or
    (board[3] == letter and board[5] == letter and board[7] == letter))

def is_board_full(board):
    return not ' ' in board

print("Hi, let's start game of Tic-Tac-Toe!")
print_board(board)

while True:
    # Player's move
    position = int(input("Enter your move (1-9): "))
    if space_is_free(position):
        insert_board('X', position)
    else:
        print("This position is already taken")
        continue

    # Check if the game is over
    if is_winner(board, 'X'):
        print_board(board)
        print("You won!")
        break
    
    if is_board_full(board):
        print_board(board)
        print("Tie game!")
        break

    # Computer's move
    for move in range(1, 10):
        if space_is_free(move):
            insert_board('O', move)
            if is_winner(board, 'O'):
                print_board(board)
                print("Sorry, you lost. The computer won.")
                break
            insert_board(' ', move)
    else:
        import random
        move = None
        possible_moves = [x for x, letter in enumerate(board) if letter == ' ']
        if len(possible_moves) > 0:
            move = random.choice(possible_moves)
            insert_board('O', move)

    # Check if the game is over
    if is_winner(board, 'O'):
        print_board(board)
        print("Sorry, you lost. The computer won.")
        break

    if is_board_full(board):
        print_board(board)
        print("Tie game!")
        break
   
    print_board(board)
