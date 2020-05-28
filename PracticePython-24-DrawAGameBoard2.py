import numpy as np

symbols = [' ', 'X', 'O']


def drawSqBoard(number, boardState):
    if number < 1:
        return 'Sorry. Please enter a number greater than or equal to 1'
    else:
        print(number * ' ---')
        for numX in range(number):
            trow = '| '
            brow = ''
            for numY in range(number):
                trow += (symbols[boardState[numX, numY]] + ' | ')
                brow += ' ---'
            print(trow)
            print(brow)


if __name__ == '__main__':
    game = np.array([[1, 2, 0], [2, 1, 0], [2, 1, 0]])
    drawSqBoard(3, game)
    print(game)
