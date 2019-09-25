x = int(input())
y = int(input())

delta = y - x + 1

if (y % delta == 0) and ((x - 1) % delta == 0):
    print('YES')
else:
    print('NO')
