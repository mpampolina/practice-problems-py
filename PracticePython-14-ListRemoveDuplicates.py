names = ['Sara', 'James', 'Oliver', 'Charlie', 'Eva', 'Charlie', 'Irene', 'Isabelle', 'Constantine', 'James', ]

unique_names = []   # my first solution using loops
names.sort()
unique_names.append(names[0])
for name in names:
    if name != unique_names[0]:
        unique_names.insert(0, name)
unique_names.sort()
print(unique_names)

unique_names2 = list(set(names))    # my second solution using sets
unique_names2.sort()
print(unique_names2)

unique_names3 = []
for name in names:
    if name not in unique_names3:
        unique_names3.append(name)
unique_names3.sort()
print(unique_names3)
