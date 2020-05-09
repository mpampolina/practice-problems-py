import itertools

def transpose(table):
    transposed_list = list(map(list, itertools.zip_longest(*table, fillvalue='-')))
    return transposed_list