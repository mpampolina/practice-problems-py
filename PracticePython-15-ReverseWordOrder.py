def reversal(sentence):     # My first solution
    sentence_components = sentence.split(' ')
    index = (len(sentence_components)-1)
    reversed = []
    for count in range(len(sentence_components)):
        reversed.append(sentence_components[index])
        index -= 1
    return ' '.join(reversed)


def reversal2(sentence):        # My second solution
    sentence_components = sentence.split(' ')
    reversed2 = []
    for component in sentence_components:
        reversed2.insert(0, component)
    return ' '.join(reversed2)


def reversal3(sentence):
    sentence_components = sentence.split(' ')
    sentence_components.reverse()          # the .reverse() method modifies the string in place (i.e. no return)
    return ' '.join(sentence_components)


userinput = input('Please enter a sentence')
print(reversal(userinput))
print(reversal2(userinput))
print(reversal3(userinput))
