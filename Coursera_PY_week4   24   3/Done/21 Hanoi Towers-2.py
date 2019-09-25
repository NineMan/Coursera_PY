def move(n, x, y):
    if n == 0:
        return
    elif n != 0:
        move(n - 1, x, SUM_TOWER - x - y)
        print(n, x, y)
        move(n - 1, SUM_TOWER - x - y, y)
        return


SUM_TOWER = 1 + 2 + 3
n = int(input())
move(n, 1, 3)
