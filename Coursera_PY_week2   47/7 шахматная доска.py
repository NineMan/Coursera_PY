a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())

if (a1 > b1):
    x = a1 - b1
else:
    x = b1 - a1

if (a2 > b2):
    y = a2 - b2
else:
    y = b2 - a2

if ((x + y) % 2 == 0):
    print('YES')
else:
    print('NO')
