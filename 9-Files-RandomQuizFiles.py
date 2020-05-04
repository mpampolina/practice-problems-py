#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
# The quiz data. Keys are states and values are their capitals.

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
            'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


def getkeys(diction):       # returns a list of keys from a given dictionary
    keylist = []
    for key in diction.keys():
        keylist.append(key)
    return keylist


def getvalues(diction):     # returns a list of values from a given dictionary
    valuelist = []
    for value in diction.values():
        valuelist.append(value)
    return valuelist


def generatemc(key, diction, valuelist):        # generates a randomized list of m/c values
    mc = []
    mc.append(diction[key])                     # appends correct answer
    wrng_ans = random.sample(valuelist, 3)      # appends wrong answers
    for ans in wrng_ans:
        mc.append(ans)
    random.shuffle(mc)                          # randomizes answer list
    return mc


import os

# Titles
path = 'e:\\'
folderTitle = 'us_capitals_quizzes\\'
keyFolderTitle = 'us_capitals_keys\\'
fileTitle = 'us_capitals_quiz_ver'
keyTitle = 'us_capitals_quiz_key'
quizTitle = 'US State Capitals Quiz'

# Make Directories for both quizzes and answer keys
os.mkdir(f'{path}{folderTitle}')
os.mkdir(f'{path}{keyFolderTitle}')

# Generate 'n' number of quiz files.
for quizNum in range(2):

    # Create the quiz and answer key files.
    cap_quiz = open(f'{path}{folderTitle}{fileTitle}_{quizNum + 1}.txt', 'w')
    cap_quiz_ans = open(f'{path}{keyFolderTitle}{keyTitle}_{quizNum + 1}.txt', 'w')

    # Write out the header for the quiz.
    cap_quiz.write('Name:\n\n\n')
    cap_quiz.write('Date:\n\n\n')
    cap_quiz.write('Period:\n\n\n')
    cap_quiz.write(f'{quizTitle} (version: {quizNum + 1})'.center(45, '-'))
    cap_quiz.write('\n\n')

    # Write out the header for the key.
    cap_quiz_ans.write(f'{quizTitle} - Key (version: {quizNum + 1})'.center(45, '-'))
    cap_quiz_ans.write('\n\n')

    # Shuffle the order of the states.
    key_list = getkeys(capitals)
    value_list = getvalues(capitals)
    random.shuffle(key_list)
    count = 1

    # Loop through all 50 states, making a question for each.
    for key in key_list:
        answer = capitals[key]
        multichoice = generatemc(key, capitals, value_list)     # returned list of m/choices, with embedded answer
        cap_quiz.write(f'Question {count}: The capital of {key} is: \n\n')
        cap_quiz_ans.write(f'Question {count}: The capital of {key} is : {answer} \n\n')
        leader = 'A'
        for index in range(4):
            cap_quiz.write(f'{leader}: {multichoice[index]}'.rjust(30, ' '))
            cap_quiz.write('\n\n')
            leader = chr(ord(leader) + 1)                                           # increments m/c leader
        count += 1

    # Close files
    cap_quiz.close()
    cap_quiz_ans.close()