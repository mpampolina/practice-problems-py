import os, re

path = 'e:\\RegexSearch'


def regexsearch(regex):
    direct = []
    for folderName, subFolders, filenames in os.walk(path):
        for file in filenames:
            if file.endswith('.txt'):
                matchfile = open(os.path.join(folderName, file), 'r')
                content = matchfile.read()
                if bool(UserRegex.search(content)):
                    direct.append(os.path.join(folderName, file))
                matchfile.close()
    return direct


print('.txt Phrase Searcher'.center(30, '-'))
phrase = input('Please input the a search phrase: \n')
phrase = phrase.replace(' ', '\s')
UserRegex = re.compile(fr'''
{phrase}
''', re.VERBOSE)
if bool(regexsearch(UserRegex)):
    print('We have found the following .txt files that match your search phrase:')
    print('\n'.join(regexsearch(UserRegex)))
else:
    print('Sorry, we were not able to find the phrase you were looking for in the .txt files within this directory.')