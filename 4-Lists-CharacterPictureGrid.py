grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def transpose(table):
    transposed_table = []
    listlength = len(grid)  # 9
    valuelength = len(grid[0])  # 6
    for sublist in range(valuelength):  # 6 new sublists
        newsublist = []
        for value in range(listlength):  # 9 new values
            newsublist.append(grid[value][sublist])  # Building a newsublist from the first (nth) value of every sublist
        transposed_table.append(newsublist)
    return transposed_table


transposed_grid = transpose(grid)
for innerLists in range(len(transposed_grid)):  # print each list in the transposed_grid to console
    print(''.join(transposed_grid[innerLists]))
