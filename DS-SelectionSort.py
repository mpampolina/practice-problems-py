''' Selection Sort: Selection sort is a sorting algorithm where we start by selecting the first number
as the minimum and go through a series of numbers and compare each number in sequence.
If the number compared is smaller than the minimum, then that number becomes the new minimum. Each
number in the series is compared against the current minimum until the series is exhausted. Then, the miniumum is
separated from the current series and the Selection Sort begins again with a smaller pool of numbers. The process
is repeated until the list is sorted.

Advantages over Bubble Sort:
- We are not switching every iteration (Selection sort will switch a maximum of once per iteration)
- The sorting list becomes shorter every iteration
'''

x = [4, 6, 2, 8, 7]

# Selection sort algorithm - My Attempt


def ssort(lis):
    clis = lis.copy()
    ilen = len(clis)
    nlis = []

    while clis:
        minimum = clis[0]
        for i in range(ilen):
            if clis[i] < minimum:
                minimum = clis[i]
        clis.remove(minimum)
        nlis.append(minimum)
        ilen -= 1

    return nlis


print(ssort(x))

# Selection sort algorithm - DS Solution
# Notes:
# LINE 40:
# indexing_length goes to the len(x)-1 position as naturally when the selection sort is run, it will push the minimum
# elements to the left positions. We do not look at the rightmost position because at the end of the sort we know it
# will be the maximum value.
# LINE 56 & 60:
# these two conditionals in combination cycle through every value but the first indexing value. The for conditional
# shifts alongside the indexing value. If the first indexing value in that iteration is the minimum,
# the if statement will not activate. Otherwise the first indexing value will shift with the index value of the
# current minimum.


def selection_sort(list_a):
    indexing_length = range(0, len(list_a)-1)

    for i in indexing_length:
        min_index = i

        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_index]:
                min_index = j

        if min_index != i:
            list_a[min_index], list_a[i] = list_a[i], list_a[min_index]

    return list_a


print(selection_sort(x))
