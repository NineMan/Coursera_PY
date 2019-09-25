a, b, c, d = int(input()), int(input()), int(input()), int(input())

if a == 0 and b == 0:
    print('INF')
if a == 0 and b != 0:
    print('NO')
if a != 0 and b == 0:
    if d == 0:
        print('NO')
    else:
        print(0)
if a != 0 and b != 0:
    if c != 0 and b / a == d / c:
        print('NO')
    elif b % a == 0:
        print(int(-b / a))
    else:
        print('NO')
