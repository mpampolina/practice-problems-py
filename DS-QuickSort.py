'''Quick Sort: Quick sort is a sorting algorithm where we start by selecting a number as the pivot value. The pivot
value can be any value such as the first, last, middle, or median. Then, the remaining values are sorted into two bins:
values greater than our pivot and less than our pivot. The pivot is then locked and the quicksort algorithm is performed
on the less/greater than bins. The process repeats again and again. In the case where there are two locked values
(previous pivots) to either side of the unsorted value, the unsorted value is then known to be in the correct position
and is locked.
'''

# Insertion sort algorithm - My Attempt

x = [0, 9, 3, 8, 2, 7, 5]


def listExist(lis):     # check if there is a value in a list with the 'list' data type
    listExists = False
    for val in lis:
        if type(val) is list:
            listExists = True
    return listExists


def srt(l):     # takes a list
    slis = l.copy()
    p = slis[0]     # uses the first value as the pivot
    slis.remove(p)      # removes the pivot value from the list

    greater = []    # creates two lists of values greater/less than pivot
    lower = []
    for val in slis:
        if val > p:
            greater.append(val)
        elif val <= p:
            lower.append(val)

    return lower, p, greater    # returns a tuple: ([values smaller than pivot], pivot, [values greater than pivot])


def Qsort(lis):             # "lis" refers to the master list
    lis = list(srt(lis))    # converts tuple to a list: [[values smaller], pivot, [values greater]]
    d = listExist(lis)      # boolean checking if there is a list value in the master list
    while d:
        for val in lis:
            if type(val) is list:
                if len(val) == 1:                   # if the sublist only contains one character:
                    lis[lis.index(val)] = val[0]    # replace the sublist with the inner character "fixing it"
                elif len(val) == 0:                 # else if the sublist is empty: remove that sublist
                    lis.remove(val)
                else:                               # else:
                    y = list(srt(val))              # perform the srt() function on the sublist (same as line 38)
                    q = lis.index(val)              # find the index of the sublist in the master list
                    lis.remove(val)                 # remove the sublist from the master list
                    for i in range(3):
                        lis.insert(q + i, y[i])     # insert the list(tuple) where the sublist was
        d = listExist(lis)                      # reassess whether there is a list in the master list
    return lis


print(Qsort(x))


# Quick sort algorithm - DS Solution


def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()     # removes the last element from the sequence and returns that element

        items_greater = []
        items_lower = []

        for item in sequence:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)    # list concatenation


print(quick_sort(x))


# Essentially the DS solution is using recursion to break down the chain of sublists into smaller and smaller
# sublists until a sublist of one or zero is avaliable. Then the single/empty character sublist is returned to the the
# previous callings of quicksort() and concatenated into bigger sublists. This is performed up the chain until a sorted
# master sublist is achieved!

# As an example of what is going on:

# We are quicksorting: [9, 5, 3, 9, 7, 8, 6, 3, 1, 6]
# items lower: [5, 3, 6, 3, 1]  - 1st iteration on master -> [6]
# pivot: [6]
# items greater: [9, 9, 7, 8]
# items lower: []               - 1st iteration on items lower
# pivot: [1]
# items greater: [5, 3, 6, 3]
# items lower: [3]              - 2nd iteration on items lower
# pivot: [3]
# items greater: [5, 6]
# items lower: [5]              - 3rd iteration on items lower -> [1, 3, 3, 5, 6]
# pivot: [6]
# items greater: []
# items lower: [7]              - 1st iteration on items greater
# pivot: [8]
# items greater: [9, 9]
# items lower: [9]              - 2nd iteration on items greater -> [8, 9, 9]
# pivot: [9]
# items greater: []
# [1, 3, 3, 5, 6, 6, 7, 8, 9, 9]    -> [1, 3, 3, 5, 6] + [6] + [7, 8, 9, 9]


