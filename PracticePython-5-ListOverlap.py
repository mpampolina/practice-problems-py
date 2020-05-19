a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

uniList = []
for num1 in a:
    if num1 in b and num1 not in uniList:
        uniList.append(num1)
print(uniList)

print(list(set([number for number in a if number in b])))
