import random
RPS = ['rock', 'paper', 'scissors']


def game():
    print("This is a best of three rock paper scissors match!")
    i = 3
    uscore, cscore = 0, 0
    while i > 0:
        choice = input("Please enter your choice of 'rock', 'paper', or 'scissors: ").lower()
        while choice not in RPS:
            print("Sorry. Your choice is invalid. Please try again")
            choice = input("\nPlease enter your choice of 'rock', 'paper', or 'scissors: ").lower()
        computer = random.choice(RPS)
        if RPS[RPS.index(choice)-1] == computer:
            uscore += 1
            print(f"\nYou Win. The computer picked {computer}\nThe score is user:{uscore}, computer:{cscore}")
        elif choice == computer:
            print(f"\nIt's a tie. The computer picked {computer}\nPlay again!\n")
            continue
        else:
            cscore += 1
            print(f"\nYou Lose. The computer picked {computer}\nThe score is user:{uscore}, computer:{cscore}")
        i -= 1
    print("\n\n")
    if uscore > cscore:
        print("You won. Congratulations!".center(50, '-'))
    else:
        print("You lost. Better luck next time!".center(50, '-'))


if __name__ == "__main__":
    game()
