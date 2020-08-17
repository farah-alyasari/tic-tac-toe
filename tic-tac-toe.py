# author: farah alyasari


# packages
import random
import sys

# make an empty board
board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
min = 1
max = 9
player_symbol = "O"
computer_symbol = "X"

#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#


def DisplayBoard(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

#
# the function accepts the board current status,
# asks the user about their move,
# checks the input and updates the board according to the user's decision,
# the number must be valid and cannot point to a field that's already occupied
#


def EnterMove(board):
    move = 0
    enteredMove = True
    while enteredMove is True:
        try:
            move = int(input("Pick a move: "))
            assert move <= max and move >= min
        except AssertionError:
            print("Illegal move")
        except ValueError:
            print("Illegal value")
        except KeyboardInterrupt:
            print("Okay, bye")
            sys.exit()
        except BaseException as e:
            print(e)
        for row in board:
            if move in row:
                move_position = row.index(move)
                row[move_position] = player_symbol
                enteredMove = False
        else:
            print("Sorry, ", move, " is occupied")


#
# Browses the board and builds a list of all the free squares;
# list consists of tuples, while each tuple is a pair of row and column numbers
#

def MakeListOfFreeFields(board):
    list = []
    for row in board:
        for col in row:
            if col != player_symbol and col != computer_symbol:
                row_position = board.index(row)
                col_position = row.index(col)
                list.append((row_position, col_position))
    return list

#
# the function analyzes the board status in order to check if
# the player using the specified symbol has won the game
#


def VictoryFor(board, symbol):
    # check if there's a win
    cross_1 = cross_2 = True
    for rc in range(3):
        # checking each possible row combination
        if (board[rc][0] == symbol and
            board[rc][1] == symbol and
                board[rc][2] == symbol):
            return True
        # check each column
        if (board[0][rc] == symbol and
            board[1][rc] == symbol and
                board[2][rc] == symbol):
            return True
        # check the diagnols
        if board[rc][rc] != symbol:
            cross_1 = False
        if board[2 - rc][2 - rc] != symbol:
            cross_2 = False
    if cross_1 or cross_2:
        return True
    return False

#
# the function draws the computer's move and updates the board
# it randomly generates a move based on the available position
#


def DrawMove(board):
    try:
        sequence = MakeListOfFreeFields(board)
        move = random.choice(sequence)
        row = move[0]
        col = move[1]
        board[row][col] = computer_symbol
    except IndexError:
        print("The game should have ended. We shouldn't reach here")
    except BaseException:
        print("unkown error. We shouldn't reach here")

#
# Program entry and program exit
#


def TicTacToe(board):
    free_fields = MakeListOfFreeFields(board)
    computer_turn = True
    computer_status = False
    player_status = False
    while(len(free_fields) > 0):
        if computer_turn:
            print("computer turn: ")
            DrawMove(board)
            computer_status = VictoryFor(board, computer_symbol)
        else:
            EnterMove(board)
            player_status = VictoryFor(board, player_symbol)
        # check victory
        if player_status is True:
            DisplayBoard(board)
            print("You won")
            break
        if computer_status is True:
            DisplayBoard(board)
            print("Computer won")
            break
        computer_turn = not computer_turn
        free_fields = MakeListOfFreeFields(board)
        DisplayBoard(board)
    if computer_status is False and player_status is False:
        print("Tie")


TicTacToe(board)
