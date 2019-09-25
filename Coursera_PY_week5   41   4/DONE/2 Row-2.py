a, b = int(input()), int(input())

i = 1
if a > b:
    i = -1

for n in range(a, b + i, i):
    print(n, end=" ")
