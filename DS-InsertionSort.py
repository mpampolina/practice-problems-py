''' Insertion Sort: Insertion sort, like Selection sort, is a sorting algorithm with two sublists: sorted and unsorted.
We start the process by selecting the first number and placing that number in our sorted sublist.
Then, we take the next value, move it to the sorted sublist in the rightmost position and compare it to the numbers
to its left, swapping whenever the immediate left value in the sorted sublist is larger.
For example, we place a number (say 5) into our sorted sublist and compare it to the number before it
(to the left, say 7). If the number before it is larger, (it is) then the two numbers swap and the number (5)
is again compared to the number to its left (say 4). As 4 is less than 5 the numbers don't swap and algorithm iterates
again with another number from the unsorted sublist.
'''

x = [3, 2, 5, 7, 4]

# Insertion sort algorithm - My Attempt


def Isort(lis):
    indexlength = len(lis) - 1

    # note that at the end of every for loop, i is reassigned normally so until then i can be altering to your choosing
    for i in range(0, indexlength):
        while lis[i] > lis[i+1]:
            lis[i+1], lis[i] = lis[i], lis[i+1]
            if i-1 >= 0:
                i -= 1
    return lis


print(Isort(x))


# Insertion sort algorithm - DS Solution

def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i > 0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i - 1

    return list_a


print(insertion_sort(x))

