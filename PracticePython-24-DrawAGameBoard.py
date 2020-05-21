def drawSqBoard(number):
    if number < 1:
        return 'Sorry. Please enter a number greater than or equal to 1'
    else:
        print(number * ' ---')
        for num in range(number):
            print('|' + number * ((3 * ' ') + '|'))
            print(number * ' ---')


if __name__ == '__main__':
    drawSqBoard(3)
