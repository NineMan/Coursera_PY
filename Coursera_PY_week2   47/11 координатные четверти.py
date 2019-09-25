x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (x1 > 0):
    x1 = 1
elif (x1 < 0):
    x1 = -1
else:
    x1 = 0

if (x2 > 0):
    x2 = 1
elif (x2 < 0):
    x2 = -1
else:
    x2 = 0

if (y1 > 0):
    y1 = 1
elif (y1 < 0):
    y1 = -1
else:
    y1 = 0

if (y2 > 0):
    y2 = 1
elif (y2 < 0):
    y2 = -1
else:
    y2 = 0


if (x1 == x2) and (y1 == y2):
    print('YES')
else:
    print('NO')
