a, b = int(input()), int(input())

for i in range(a, b + 1):
    x = str(i)
    if x[0] == x[3] and x[1] == x[2]:
        print(i)
