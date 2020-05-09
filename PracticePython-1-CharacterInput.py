from datetime import datetime
now_date = datetime.date(datetime.now())
curr_year = now_date.year

try:
    name = input('Hello user.\nPlease enter your name: \n')
    age = input('Please enter your age: \n')
    numMsg = input('Please enter the number of messages to send.\n')
    cent_year = curr_year + (100 - int(age))
    for iterations in range(int(numMsg)):
        print(f'{name}.\nYou will be 100 years old in the year {cent_year}')
except ValueError as err:
    print('Error! Try again. Please enter an integer value as your age.')
