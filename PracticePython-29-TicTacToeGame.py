import numpy as np
players = [1, 2]
symbols = [' ', 'X', 'O']

game = np.zeros((3, 3))


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


def checkCols(board, player):
    # print(np.all(board == 2, axis=0))
    if np.any(np.all(board == player, axis=0)):
        print(f'there is a column of {player}s!' + '\n' + f'player: {player} wins!')
        return True


def checkRows(board, player):
    # print(np.all(board == 2, axis=1))
    if np.any(np.all(board == player, axis=1)):
        print(f'there is a row of {player}s!' + '\n' + f'player: {player} wins!')
        return True


def checkDiag(board, player):
    # print(board[[0,1,2],[0,1,2]] == 1)
    # print(board[[0,1,2],[2,1,0]] == 1)
    if np.any(np.all(board[[0, 1, 2], [0, 1, 2]] == player)):
        print(f'there is a diagonal row of {player}s!' + '\n' + f'player: {player} wins!')
        return True
    elif np.any(np.all(board[[0, 1, 2], [2, 1, 0]] == player)):
        print(f'there is a diagonal row of {player}s!' + '\n' + f'player: {player} wins!')
        return True


def checkGrid(grid):
    for play in players:
        if np.any([checkCols(grid, play), checkRows(grid, play), checkDiag(grid, play)]):
            return False


def rebuild(gameboard):
    switch = game.copy()
    topRow = game[0, :].copy()  # switch top and bottom rows to account for standard cartesian plane coordinates
    botRow = game[2, :].copy()
    switch[0] = botRow
    switch[2] = topRow
    return switch.astype(dtype="int32")


def playermove(player, symbol):
    user = input(f'Player {player} ({symbol}), Please input your move coordinates in the form "x y": ').split()
    arr = np.array(user, dtype='int32')
    arr -= 1    # convert to 0 index
    if game[arr[1], arr[0]] == 0:
        game[arr[1], arr[0]] = player
        drawSqBoard(3, rebuild(game))
        return game
    else:
        print("Sorry. Place taken. Please try again")
        playermove(player, symbol)


if __name__ == '__main__':
    gameContinue = True
    print("Welcome to Classic TicTacToe")
    drawSqBoard(3, rebuild(game))
    while gameContinue is not False:
        for i in range(2):
            grid = playermove(players[i], symbols[players[i]])
            gameContinue = checkGrid(grid)
            if gameContinue is False:
                break
