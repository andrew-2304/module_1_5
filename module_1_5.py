immutable_var = ('Andrey', 1, True)
print(immutable_var)
# TypeError: 'tuple' object does not support item assignment
mutable_list = ['Raev', 2, False]
print(mutable_list)
mutable_list[1] = 3
mutable_list.append(4)
print(mutable_list)