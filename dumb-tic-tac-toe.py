import random
import os
from colorama import init
from termcolor import colored

if __name__ == "__main__":
    main()


def main():
    init()
    Welcome()


def Welcome():
    os.system("cls" if os.name == "nt" else "clear")
    play = input(
        "\nWould you like to play the dumb tic-tac-toe game? Enter 'p' to play or 'q' to quit : "
    )
    os.system("cls" if os.name == "nt" else "clear")
    if play == "p":
        availableChoices = []
        plays = []
        PlayGame(availableChoices, plays)
    if play == "q":
        SystemExit
    if not ((play == "p") or (play == "q")):
        print("Invalid choice. Please try again")
        Welcome()


def GameBoard(availableChoices, plays):
    os.system("cls" if os.name == "nt" else "clear")
    print("\n")
    GameBoardColor(0)
    print("|", end=" ")
    GameBoardColor(1)
    print("|", end=" ")
    GameBoardColor(2)
    print("\n")
    GameBoardColor(3)
    print("|", end=" ")
    GameBoardColor(4)
    print("|", end=" ")
    GameBoardColor(5)
    print("\n")
    GameBoardColor(6)
    print("|", end=" ")
    GameBoardColor(7)
    print("|", end=" ")
    GameBoardColor(8)
    print("\n")


def GameBoardColor(availableChoices, plays, choice):
    if plays[choice] == "X":
        print(colored(plays[choice], "green"), end=" ")
    elif plays[choice] == "O":
        print(colored(plays[choice], "red"), end=" ")
    else:
        print(plays[choice], end=" ")


def PlayGame(availableChoices, plays):
    availableChoices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    plays = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    gameStatus = -1
    GameBoard(plays)
    while gameStatus == -1:
        TurnUser()
        GameBoard(plays)
        gameStatus = CheckWin()
        TurnComputer()
        GameBoard(plays)
        gameStatus = CheckWin()
    if gameStatus == 1:
        print("\nCongratulations! You have won the game. Thank you for playing")
        SystemExit
    if gameStatus == 0:
        print("\nOops! You have lost the game. Thank you for playing")
        SystemExit


def TurnUser(availableChoices, plays):
    choice = int(input("\nEnter the position where you want to play this round : "))
    if choice < 9:
        if choice in availableChoices:
            plays[choice] = "X"
            availableChoices.remove(choice)
        else:
            print("The position is already filled, try again!")
            TurnUser()
    else:
        print("Invalid position, try again!")
        TurnUser()


def TurnComputer(availableChoices, plays):
    choice = random.choice(availableChoices)
    plays[choice] = "O"
    availableChoices.remove(choice)


def CheckWin(availableChoices, plays):
    if plays[0] == plays[1] and plays[1] == plays[2] and plays[2] == "X":
        return 1
    if plays[3] == plays[4] and plays[4] == plays[5] and plays[5] == "X":
        return 1
    if plays[6] == plays[7] and plays[7] == plays[8] and plays[8] == "X":
        return 1
    if plays[0] == plays[3] and plays[3] == plays[6] and plays[6] == "X":
        return 1
    if plays[1] == plays[4] and plays[4] == plays[7] and plays[7] == "X":
        return 1
    if plays[2] == plays[5] and plays[5] == plays[8] and plays[8] == "X":
        return 1
    if plays[0] == plays[4] and plays[4] == plays[8] and plays[8] == "X":
        return 1
    if plays[2] == plays[4] and plays[4] == plays[6] and plays[6] == "X":
        return 1
    if plays[0] == plays[1] and plays[1] == plays[2] and plays[2] == "O":
        return 0
    if plays[3] == plays[4] and plays[4] == plays[5] and plays[5] == "O":
        return 0
    if plays[6] == plays[7] and plays[7] == plays[8] and plays[8] == "O":
        return 0
    if plays[0] == plays[3] and plays[3] == plays[6] and plays[6] == "O":
        return 0
    if plays[1] == plays[4] and plays[4] == plays[7] and plays[7] == "O":
        return 0
    if plays[2] == plays[5] and plays[5] == plays[8] and plays[8] == "O":
        return 0
    if plays[0] == plays[4] and plays[4] == plays[8] and plays[8] == "O":
        return 0
    if plays[2] == plays[4] and plays[4] == plays[6] and plays[6] == "O":
        return 0
    return -1
