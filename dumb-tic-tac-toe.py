import random
import os
from colorama import init
from termcolor import colored


def Welcome():
    clear_console()
    play = input(
        "\nWould you like to play the dumb tic-tac-toe game? Enter 'p' to play or 'q' to quit : "
    )
    os.system("cls" if os.name == "nt" else "clear")
    if play == "p":
        PlayGame()
    if play == "q":
        SystemExit
    if not ((play == "p") or (play == "q")):
        print("Invalid choice. Please try again")
        Welcome()


def PlayGame():
    availableChoices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    plays = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    gameStatus = -1
    GameBoard(plays)
    while gameStatus == -1:
        availableChoices, plays = TurnUser(availableChoices, plays)
        GameBoard(plays)
        gameStatus = CheckWin(plays)
        if gameStatus != -1:
            break
        availableChoices, plays = TurnComputer(availableChoices, plays)
        GameBoard(plays)
        gameStatus = CheckWin(plays)
        if gameStatus != -1:
            break
    if gameStatus == 1:
        print("\nCongratulations! You have won the game. Thank you for playing.")
        SystemExit
    if gameStatus == 0:
        print("\nOops! You have lost the game. Thank you for playing.")
        SystemExit


def GameBoard(plays):
    clear_console()
    print("\n")
    GameBoardColor(plays, 0)
    print("|", end=" ")
    GameBoardColor(plays, 1)
    print("|", end=" ")
    GameBoardColor(plays, 2)
    print("\n")
    GameBoardColor(plays, 3)
    print("|", end=" ")
    GameBoardColor(plays, 4)
    print("|", end=" ")
    GameBoardColor(plays, 5)
    print("\n")
    GameBoardColor(plays, 6)
    print("|", end=" ")
    GameBoardColor(plays, 7)
    print("|", end=" ")
    GameBoardColor(plays, 8)
    print("\n")


def GameBoardColor(plays, choice):
    if plays[choice] == "X":
        print(colored(plays[choice], "green"), end=" ")
    elif plays[choice] == "O":
        print(colored(plays[choice], "red"), end=" ")
    else:
        print(plays[choice], end=" ")


def CheckWin(plays):
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


def TurnUser(availableChoices, plays):
    choice = int(
        input("\nEnter the position where you want to play this round : "))
    if choice < 9:
        if choice in availableChoices:
            plays[choice] = "X"
            availableChoices.remove(choice)
        else:
            print("The position is already filled, try again!")
            TurnUser(availableChoices, plays)
    else:
        print("Invalid position, try again!")
        TurnUser(availableChoices, plays)
    return availableChoices, plays


def TurnComputer(availableChoices, plays):
    choice = random.choice(availableChoices)
    plays[choice] = "O"
    availableChoices.remove(choice)
    return availableChoices, plays


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    init()
    Welcome()
