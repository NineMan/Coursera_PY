def move(n, x, y):
    if n == 0:
        print(0)
    elif n == 1:
        print(x, y)
        return
    elif n != 1:
        if n == 2:
            print(n - 1, end=' ')
        move(n - 1, x, SUM_TOWER - x - y)
        print(n, end=' ')
        move(1, x, y)
        if n == 2:
            print(n - 1, end=' ')
        move(n - 1, SUM_TOWER - x - y, y)
        return


SUM_TOWER = 1 + 2 + 3
n = int(input())
if n == 1:
    print(n, 1, 3)
elif n > 1:
    move(n, 1, 3)
