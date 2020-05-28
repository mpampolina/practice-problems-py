import numpy as np

game = np.zeros((3, 3))

print(game)


def rebuild(gameboard):
    switch = game.copy()
    topRow = game[0, :].copy()  # switch top and bottom rows to account for standard cartesian plane coordinates
    botRow = game[2, :].copy()
    switch[0] = botRow
    switch[2] = topRow
    return switch


def playermove(player, symbol):
    user = input(f'Player {player} ({symbol}), Please input your move coordinates in the form "x y": ').split()
    arr = np.array(user, dtype='int32')
    arr -= 1    # convert to 0 index
    if game[arr[1], arr[0]] == 0:
        game[arr[1], arr[0]] = player
        print(rebuild(game))
    else:
        print("Sorry. Place taken. Please try again")
        playermove(player, symbol)

# userO = [input('Player 2 (O), Please input your move coordinates in the form "x y": ').split()]
for num in range(9):
    playermove(1, 'X')
    playermove(2, 'O')
