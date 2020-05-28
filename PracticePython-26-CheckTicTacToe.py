import numpy as np
players = [1, 2]

game = np.array([[1, 2, 0], [2, 1, 0], [2, 1, 0]])
winIs2 = np.array([[2, 2, 0], [2, 1, 0], [2, 1, 1]])
winIs22 = np.array([[1, 2, 1], [2, 2, 2], [1, 0, 1]])
winIs1 = np.array([[1, 2, 0], [2, 1, 0], [2, 1, 1]])
winIs11 = np.array([[0, 1, 0], [2, 1, 0], [2, 1, 1]])
winIs12 = np.array([[0, 1, 0], [2, 1, 0], [2, 1, 1]])
nowin = np.array([[1, 2, 0], [2, 1, 0], [2, 1, 2]])
nowin2 = np.array([[1, 2, 0], [2, 1, 0], [2, 1, 0]])

print(game)
print(winIs2)
print(winIs22)
print(winIs11)
print('\n')


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


def checkgrid(grid):
    for play in players:
        if np.any([checkCols(grid, play), checkRows(grid, play), checkDiag(grid, play)]):
            return True

# checkCols(winIs2, 2)
# checkRows(winIs22, 2)
# checkDiag(winIs1, 1)
# print(checkgrid(game))
print(checkgrid(winIs1))
# print(winIs2.shape[1])
