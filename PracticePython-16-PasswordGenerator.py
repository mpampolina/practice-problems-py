import random
import string

numerical = [str(i) for i in range(0, 10)]
symbolic = ['_', '-', '!', '@', '#', '$', '%', '^', '&', '*']
lowletters = list(string.ascii_lowercase)
capletters = list(string.ascii_uppercase)
types = [capletters, lowletters, symbolic, numerical]
password = []
for type in types:
    for char in range(random.randint(3, 5)):
        password.append(random.choice(type))
random.shuffle(password)
print(''.join(password))
