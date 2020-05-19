p1 = 'Rotator'
p2 = 'hannah'
p3 = 'Do geese see god'
p4 = 'Draw a game board'
p5 = 'racecar'
p6 = 'PracticePython'


def remspace(sentence):
    lis = list(sentence)
    for i in lis:
        if i == ' ':
            lis.remove(' ')
    return lis


def palen(word):
    l = remspace(word.lower())
    for i in range(len(l)):
        if l[i] != l[-(i + 1)]:
            return "not palendrome"
    return "palendrome"


print(palen(p1))
