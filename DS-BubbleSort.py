''' Bubble Sort: Bubble sort is a sorting algorithm where we go through a series of numbers and grab
two consecutive numbers (i.e. 4 and 6) and compare them. If the first number is higher than the second,
we switch the two numbers. If the first number is lower than the second, we leave the two numbers as is.
We iterate through the series of numbers until the list is sorted and no more switching takes place
'''

x = [4, 6, 8, 3, 2, 5, 7, 8, 9]

# Bubble sort algorithm - My Attempt
# Note: in hindsight my program is very convoluted but it works hehe xD


def pairwise(l):
    return zip(l, l[1:])


def bsort(lis):
    rounds = 0
    nlis = lis.copy()
    for index, pair in enumerate(tuple(pairwise(lis))):
        f = pair[0]
        s = pair[1]
        if f > s:
            nlis[index], nlis[index+1] = nlis[index+1], nlis[index]
            rounds += 1
    if rounds != 0:
        bsort(nlis)
        return nlis
    else:
        return nlis


print(bsort(x))


# Bubble sort algorithm - DS Solution


def bubble(list_a):
    indexing_length = len(list_a) - 1   # cannot create a comparison with the last element
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]

    return list_a


print(bubble(x))
