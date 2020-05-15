'''Alternate intepretation: if a cow value is already placed and the digit is exhausted, the game will still register a
bull for the further instances of the value.
example: Number is 1038. Guess is 1138. System will yield: 3 cows 1 bulls.
'''
import random


def CaB(guess_num):
    cows = 0
    bulls = 0
    guess = list(str(guess_num))
    mute = list(key)    # fixes list reference error!
    for count in range(len(guess)):
        if guess[count] == key[count]:
            cows += 1
        else:
            bulls += 1
    return cows, bulls


def game(tries):
    while tries > 0:
        guessing = input('Please enter your guess: \n')
        if len(guessing) == 4 and guessing.isdecimal():
            tries -= 1
            resultC, resultB = CaB(guessing)
            print(f'{str(resultC)} cows; {str(resultB)} bulls')
            if resultC == 4:
                print('\nCongratulations! You have guessed the correct number!\n')
                break
            else:
                print(f'Try again! You have: {tries} tries remaining.')
        else:
            print('Sorry! You have to input a 4-digit number.')


if __name__ == "__main__":
    print('Welcome to the Cows and Bulls Game!')
    print('''\nRules: Guess a 4-digit number. For every digit guessed correctly in the correct place, 
    you have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull."
    Guess the correct number within 10 attempts and you win! Good Luck!\n''')
    number = random.randint(1000, 9999)
    # print(str(number))    # for testing
    key = list(str(number))
    game(10)
