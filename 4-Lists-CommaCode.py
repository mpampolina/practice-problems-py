spam = ['apples', 'bananas', 'tofu', 'cats', 'goku']
spam2 = []

def list_string(inlist):
    export = ''
    for value in range(len(inlist)):
        if value < (len(inlist) - 1):
            export = (export + inlist[value] + ', ')
        else:
            export = (export + 'and ' + inlist[value])
    return export

print(list_string(spam))
