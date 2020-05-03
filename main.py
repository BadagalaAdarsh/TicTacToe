# ---------------- Globla Varibles -------------------- #


# board is a list which I have used to display as a game board
# --------------- Game Board -------------------------#
board = [" - ", " - ", " - ",
         " - ", " - ", " - ",
         " - ", " - ", " - "]

# ---------- If game is still going ---------------------- #
game_still_going = True

# ---------- who won (or) tie ------------------------- #
winner = None

# ------------ who is currently playing ------------------ #
current_player = " X "

# --------------postion where we need to place the value --------#
position = None


# Method to display the game board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Method to play the game tic tac toe
def play_game():
    # In playing game major thing is to display the initial board
    display_board()

    # Loop to handle turns and to continue game till someone wins or its a tie
    while game_still_going:
        # Method to handle a single turn of a arbitrary player
        handle_turn(current_player)

        # To check whether is the game is complete or not
        check_if_game_over()

        # To flip between the players
        flip_player()

    # The game has ended
    if winner == " X " or winner == " O ":
        print(winner + "won.")

    elif winner is None:
        print("Its a Tie.")


# Method a handle game of a single player
def handle_turn(player):
    # declaration of global variable so that it can be modified over here
    global position

    print(player + "'s turn now.")

    # method to take the input from the user
    ask_input()

    # here we need to check whether the provided input is valid or not
    # check_input() is the method which checks whether provided input is in correct format or not
    # here in check input itself there is a method to check whether the given position is empty or not
    # I have written there because it was easier and simple checking there instead of writing the same code here
    if check_input():
        # placing value at the index specified by the user
        board[position] = player
        display_board()


def check_if_game_over():
    # Methods to check win or tie
    check_for_winner()
    check_for_tie()


def check_for_winner():
    # as winner is declared out side the method in order to write to it we need to declare it as global inside the
    # method
    global winner

    # Inorder to do this I need to check
    # rows,
    row_winner = check_rows()

    # coloumns
    coloumn_winner = check_coloumns()

    # diagonals
    diagonal_winner = check_diagonals()

    # condition to assign winner based on the game
    if row_winner:
        winner = row_winner

    elif coloumn_winner:
        winner = coloumn_winner

    elif diagonal_winner:
        winner = diagonal_winner

    else:
        winner = None

    return


def check_rows():
    # setting up of globla variables
    global game_still_going

    # check if any one of the row all are equal and not equal to empty dash "-"
    # below if all the three values are equal they'll return True
    row_1 = board[0] == board[1] == board[2] != " - "
    row_2 = board[3] == board[4] == board[5] != " - "
    row_3 = board[6] == board[7] == board[8] != " - "

    # changing the game_still_going to False so that game can end
    if row_1 or row_2 or row_3:
        game_still_going = False

    # returning value of the winner based on the row
    if row_1:
        return board[0]

    elif row_2:
        return board[3]

    elif row_3:
        return board[6]
    return


def check_coloumns():
    # same as check rows
    global game_still_going

    col_1 = board[0] == board[3] == board[6] != " - "
    col_2 = board[1] == board[4] == board[7] != " - "
    col_3 = board[2] == board[5] == board[8] != " - "

    if col_1 or col_2 or col_3:
        game_still_going = False

    if col_1:
        return board[0]

    elif col_2:
        return board[1]

    elif col_3:
        return board[2]

    return


def check_diagonals():
    # same as check_rows and check_coloumns only the values will be changing

    global game_still_going

    diag_1 = board[0] == board[4] == board[8] != " - "
    diag_2 = board[2] == board[4] == board[6] != " - "

    if diag_1 or diag_2:
        game_still_going = False

    if diag_1:
        return board[0]

    elif diag_2:
        return board[2]

    return


def check_for_tie():
    # as usual declaring global variables so that it can be modified over here in this method
    global game_still_going

    # this method can be fulfilled simply by checking whether there are any empty spaces
    # in this case these are dashes
    # if there are dashes game is not over yet else game is finished

    if " - " not in board:
        game_still_going = False

    return


def flip_player():
    # global variables that we need to change in this method
    global current_player

    # flipping of players based on the current conditions
    # that is changing from X to O or vice versa
    if current_player == " X ":
        current_player = " O "

    elif current_player == " O ":
        current_player = " X "

    return


def ask_input():
    # declaring position as global
    global position

    # asking for the user input
    position = input("Choose a postition from 1-9: ")

    return


def check_input():
    # declaring position as global for modifications if any
    global position

    # asking user input repeatedly until user provides input in the correct format
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Looks like given format is wrong. Please enter number in between 1-9: ")

    # here we are deduction -1 because in list index start from 0 not 1
    position = int(position) - 1

    # now check whether the provided input is empty or not
    if check_empty():
        # return true if user has provided valid and correct that is empty field as input or not
        return True
    else:
        position = input("This position is already filled. Please give another value: ")
        check_input()

    # returning true if user has provided input in correct format
    return True


def check_empty():
    # declaring postion as global so that it can be modified here if any
    global position

    # check whether the provided position in empty or not if Yes return True
    if board[position] == " - ":
        return True
    else:
        return False

    # # else ask input here and then check for validity and empty or not again
    # else:
    #     ask_input()


play_game()

# ------------------- My Basic Plan to Build the Game ----------------------- #
# For developing this game I need to write the logic first
# I am going to need a board
# Display the board
# Play the game (probably a method)
# Method to check win or tie
# Here I need to check rows and columns and diagnols too
# Method to filp players
