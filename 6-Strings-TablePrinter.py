tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def extract(row, table):    # Returns a list of values of the same 'row' in the list of lists (table)
    newlist = []
    for sublist in table:
        newlist.append(sublist[row])
    return newlist          # can also use: return [sublist[row] for sublist in table]


def max_col_length(table):      # Find the maximum column length in a list of lists
    largest_col = 0
    for count in range(len(table)):
        if len(tableData[count]) > largest_col:
            largest_col = len(table[count])
    return largest_col


def column_width(table):        # Find the width of a column based on the largest string in said column
    colwidths = [0] * len(table)
    for index in range(len(table)):
        longest_val = 0
        for val in table[index]:    # table[index] is a list
            if len(val) > longest_val:
                longest_val = len(val)
        colwidths[index] = longest_val
    return colwidths


def printTable():
    # Transpose tableData
    transposedtable = []
    for rownum in range(max_col_length(tableData)):
        transposedtable.append(extract(rownum, tableData))      # NOTE: extract() will not work for ragged tables

    maxchar = sum(column_width(tableData)) + (len(tableData) - 1)   # the maximum number of characters (incl. spaces)
    for subvec in transposedtable:
        export = ' '.join(subvec)
        print(export.rjust(maxchar, ' '))


printTable()
