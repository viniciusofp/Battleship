from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

print "--------"

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


for turn in range(4):
    print "Turn " + str(turn + 1)
    print "--------"
    print_board(board)
    print "--------"
    # Everything from here on should go in your for loop!
    # Be sure to indent four spaces!
    guess_row = int(raw_input("Guess Row:")) - 1
    guess_col = int(raw_input("Guess Col:")) - 1
    
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
    	if turn == 3:
    		print "---------"
    		print "You Lose!"
        elif (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4) or (guess_row == "" or guess_col == "") :
            print "Oops, that's not even in the ocean."

        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
    print "---------------"
