a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# --list comprehension version--
b = [value for value in a if value % 2 == 0]
#   create a list of values for each value in a if that value's modulus is equal to zero
print(b)

# --normal version--
even_list = []
for value in a:
    if value % 2 == 0:
        even_list.append(value)
print(even_list)
