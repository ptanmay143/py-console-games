import random

def Welcome():
    play = input(
        "\nWould you like to play the rock paper scissor game? Enter 'p' to play or 'q' to quit : "
    )
    if play == "p":
        print(
            "\nWelcome to a game of rock paper scissor.\nYou will be playing against the dumb computer.\nLet's see if you can win.\nGood Luck"
        )
        PlayGame()
    if play == "q":
        SystemExit
    if not ((play == "p") or (play == "q")):
        print("Invalid choice. Please try again")
        Welcome()


def PlayGame():
    choices = ["r", "p", "s"]
    playUser = TurnUser(choices)
    playComputer = TurnComputer(choices)
    print("\nYou chose", playUser, "and computer chose", playComputer)
    if playUser == "r":
        if playComputer == "r":
            print("Tie")
        elif playComputer == "p":
            print("You lose")
        elif playComputer == "s":
            print("You win")
    elif playUser == "p":
        if playComputer == "r":
            print("You win")
        elif playComputer == "p":
            print("Tie")
        elif playComputer == "s":
            print("You lose")
    elif playUser == "s":
        if playComputer == "r":
            print("You lose")
        elif playComputer == "p":
            print("You win")
        elif playComputer == "s":
            print("Tie")
    print("\nThank you for playing.")


def TurnUser(choices):
    print("\nEnter your choice as follows")
    print("(r)ock (p)aper (s)cissor : ")
    playUser = input()
    if playUser in choices:
        return playUser
    else:
        print("Invalid choice. Please try again.")
        TurnUser()


def TurnComputer(choices):
    playComputer = random.choice(choices)
    return playComputer

if __name__ == "__main__":
    Welcome()