import os
import time
import random


def welcome():
    for i in range(0, 11):
        print("*", end="")
    print()
    print("* WELCOME *", end="")
    print()
    for i in range(0, 11):
        print("*", end="")
    print()
    input("Press ENTER key to start")
    option()


def option():
    for i in range(0, 21):
        print("*", end="")
    print()
    print("1)StonePaperScissors\n2)TicTacToe")
    for i in range(0, 21):
        print("*", end="")
    print()
    chc = int(input("Enter your choice number: "))
    if chc == 1:
        stonepaperscissor()
    elif chc == 2:
        tictactoemenu()
    else:
        welcome()


def stonepaperscissor():
    print("STONE,PAPER,SCISSORS")
    print("You will be competing against the computer")
    print("The competitor who first scores 5 points will be declared as the winner")
    print("For Stone,Enter 0")
    print("For Paper,Enter 1")
    print("For Scissors,Enter 2")
    print("To EndGame and go back to MainMenu,Enter -1")
    user = 0
    comp = 0
    cnt = 0
    choice_play = ["Stone", "Paper", "Scissors"]
    while user < 5 and comp < 5 and cnt < 25:
        cnt += 1
        a = int(input("Enter your choice="))
        for i in range(0, 20):
            print("*", end="")
        print()
        if a == -1:
            print("Thankyou For Playing")
            welcome()
            break
        b = random.choice([0, 1, 2])
        if a == 0 and b == 1:
            comp += 1
        elif a == 0 and b == 2:
            user += 1
        elif a == 1 and b == 0:
            user += 1
        elif a == 1 and b == 2:
            comp += 1
        elif a == 2 and b == 0:
            comp += 1
        elif a == 2 and b == 1:
            user += 1
        print("You:", choice_play[a])
        print("Computer:", choice_play[b])
        print("Scores")
        print("You=", user, "\t Computer=", comp)
        for i in range(0, 20):
            print("*", end="")
        print()
        if(user > comp and user == 5):
            print("Congratulations!!You are the Winner!")
        elif(user < comp and comp == 5):
            print("Sorry!!Better luck next time!")
        elif(user == comp and cnt >= 25):
            print("Its a Draw")


def tictactoemenu():
    print("Welcome To TicTacToe")
    for i in range(0, 21):
        print("*", end="")
    print()
    print("1)TwoPlayer\n2)OnePlayer")
    for i in range(0, 21):
        print("*", end="")
    print()
    chc = int(input("Enter your choice number: "))
    if chc == 1:
        two_player()
    elif chc == 2:
        single_player()
    else:
        option()


def two_player():
    board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def rules():
        print("Welcome to TICTACTOE")
        print("This is a two player game where USER1 is X and USER2 is O")
        print("Enter your choice from 1 to 9")
        print("""
                1 | 2 | 3
                ---|---|---
                4 | 5 | 6
                ---|---|---
                7 | 8 | 9
                """)

    def print_board():
        print("   |   |   ")
        print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
        print("   |   |   ")

    def is_winner(board, player):
        if (board[1] == player and board[2] == player and board[3] == player) or \
            (board[4] == player and board[5] == player and board[6] == player) or \
            (board[7] == player and board[8] == player and board[9] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[3] == player and board[6] == player and board[9] == player) or \
            (board[1] == player and board[5] == player and board[9] == player) or \
                (board[3] == player and board[5] == player and board[7] == player):
            return True
        else:
            return False

    def is_board_full(board):
        if " " in board:
            return False
        else:
            return True

    while True:
        os.system("clear")
        rules()
        print_board()

        # user 1
        choice = input("Please choose an empty space for X: ")
        choice = int(choice)
        if board[choice] == " ":
            board[choice] = "X"
        else:
            print("Spot already taken")
            time.sleep(1)
        # for user 1 to win
        if is_winner(board, "X"):
            os.system("clear")
            rules()
            print_board()
            print("USER1 Win")
            break

        os.system("clear")
        rules()
        print_board()

        # check if board is full i.e. a tie
        if is_board_full(board):
            print("Tie")
            break

        # user 2
        choice = input("Please choose an empty space for O: ")
        choice = int(choice)
        if board[choice] == " ":
            board[choice] = "O"
        else:
            print("Spot already taken")
            time.sleep(1)
        # for user 2 to win
        if is_winner(board, "O"):
            os.system("clear")
            rules()
            print_board()
            print("USER2 Win")
            break

        # check if board is full i.e. a tie
        if is_board_full(board):
            print("Tie")
            break


def single_player():
    board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def rules():
        print("Welcome to TICTACTOE")
        print("This is a single player game where You are X and Computer is O")
        print("Enter your choice from 1 to 9")
        print("""
                1 | 2 | 3
                ---|---|---
                4 | 5 | 6
                ---|---|---
                7 | 8 | 9
                """)

    def print_board():
        print("   |   |   ")
        print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
        print("   |   |   ")

    def is_winner(board, player):
        if (board[1] == player and board[2] == player and board[3] == player) or \
            (board[4] == player and board[5] == player and board[6] == player) or \
            (board[7] == player and board[8] == player and board[9] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[3] == player and board[6] == player and board[9] == player) or \
            (board[1] == player and board[5] == player and board[9] == player) or \
                (board[3] == player and board[5] == player and board[7] == player):
            return True
        else:
            return False

    def is_board_full(board):
        if " " in board:
            return False
        else:
            return True

    def get_computer_move(board, player):

        # check for a win
        for i in range(1, 10):
            if board[i] == " ":
                board[i] = player
                if is_winner(board, player):
                    return i
                else:
                    board[i] = " "

        # check for column block
        for i in [1, 2, 3]:
            if board[i] == "X" and board[i+3] == "X" and board[i+6] == " ":
                return i+6
            if board[i+3] == "X" and board[i+6] == "X" and board[i] == " ":
                return i
            if board[i] == "X" and board[i+6] == "X" and board[i+3] == " ":
                return i+3

        # check for rows blocks
        for i in [1, 4, 7]:
            if board[i] == "X" and board[i+1] == "X" and board[i+2] == " ":
                return i+2
            if board[i+1] == "X" and board[i+2] == "X" and board[i] == " ":
                return i
            if board[i] == "X" and board[i+2] == "X" and board[i+1] == " ":
                return i+1

        # check diagonal block
        if board[1] == "X" and board[5] == "X" and board[9] == " ":
            return 9
        if board[9] == "X" and board[5] == "X" and board[1] == " ":
            return 1
        if board[1] == "X" and board[9] == "X" and board[5] == " ":
            return 5
        if board[3] == "X" and board[5] == "X" and board[7] == " ":
            return 7
        if board[7] == "X" and board[5] == "X" and board[3] == " ":
            return 3
        if board[3] == "X" and board[7] == "X" and board[5] == " ":
            return 5

        if board[5] == " ":
            return 5
        while True:
            move = random.randint(1, 9)
            if board[move] == " ":
                return move
                break
            return 5

    while True:
        os.system("clear")
        rules()
        print_board()

        # user 1
        choice = input("Please choose an empty space for X: ")
        choice = int(choice)
        if board[choice] == " ":
            board[choice] = "X"
        else:
            print("Spot already taken")
            time.sleep(1)
        # for user 1 to win
        if is_winner(board, "X"):
            os.system("clear")
            rules()
            print_board()
            print("Congratulations!!You Win")
            break

        os.system("clear")
        rules()
        print_board()

        # check if board is full i.e. a tie
        if is_board_full(board):
            print("Tie")
            break

        # user 2
        choice = get_computer_move(board, "O")
        if board[choice] == " ":
            board[choice] = "O"
        else:
            print("Spot already taken")
            time.sleep(1)
        # for user 2 to win
        if is_winner(board, "O"):
            os.system("clear")
            rules()
            print_board()
            print("Sorry!!COMPUTER Wins")
            break

        # check if board is full i.e. a tie
        if is_board_full(board):
            print("Tie")
            break


welcome()
print("\n")
option()
