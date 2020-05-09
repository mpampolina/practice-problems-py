import re
# REGEX PATTERNS
# a strong password should be at least 8 digits long
# contains uppercase and lowercase letters
# at least one digit
# at least one symbol
capRegex = re.compile(r'''(
[A-z]+
)''', re.VERBOSE)
lowRegex = re.compile(r'''(
[a-z]+
)''', re.VERBOSE)
numRegex = re.compile(r'''(
[0-9]+
)''', re.VERBOSE)
symRegex = re.compile(r'''(
[ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]+
)''', re.VERBOSE)

listRegex = [capRegex, lowRegex, numRegex, symRegex]
diagnosis = {capRegex: 'uppercase letters', lowRegex: 'lowercase letters', numRegex: 'numbers',
            symRegex:'symbols'}


def evalPassword(password):
    if len(password) < 8:
        print('Your password is not long enough (hint: a good password is at least 8 characters long!)')
        return False
    else:
        for Regex in listRegex:
            if not bool(Regex.search(password)):    # bool() reads true if a match object is returned by re.search()
                print(f'Your password is vunerable. Your password is missing: {diagnosis[Regex]}')
                return False
        return True


def evaluator():
    print('Password Strength Evaluator'.center(31, '-'))
    pass_input = input('Please enter your password: \n')
    if evalPassword(pass_input):
        print('Your password is strong')
    else:
        print('Please try again.\n')
        evaluator()


evaluator()