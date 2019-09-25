arr_of_sets = [{1, 2, 3}, {1, 3, 4, 5}, {1, 8, 9}]

x = arr_of_sets[0]
y = arr_of_sets[0]

for i in arr_of_sets:
    x |= x | i
    y &= i

print(x)
print(y)