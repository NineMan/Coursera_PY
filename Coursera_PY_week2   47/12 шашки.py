x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

up = y2 - y1
if (x2 > x1):
    vbok = x2 - x1
else:
    vbok = x1 - x2


if (up < 0):
    print('NO')
elif ((up + vbok) % 2 == 0) and (up >= vbok):
    print('YES')
else:
    print('NO')
