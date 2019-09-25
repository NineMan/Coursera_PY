a = [[1, 2], [3, 4]]

b = list(zip(*a))
print(b)

c = []
for i in b:
    c.append(list(i))
print(c)
