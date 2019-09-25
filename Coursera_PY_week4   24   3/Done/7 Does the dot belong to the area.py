a, b = float(input()), float(input())


def IsPointInArea(x, y):
    LinesUp = (y >= -x) and (y >= (2 * x + 2))
    CircleUp = (x + 1) ** 2 + (y - 1) ** 2 <= 4
    AreaUp = LinesUp and CircleUp

    LinesDown = (y <= -x) and (y <= 2 * x + 2)
    CircleDown = (x + 1) ** 2 + (y - 1) ** 2 >= 4
    AreaDown = LinesDown and CircleDown
    return (AreaUp) or (AreaDown)


if IsPointInArea(a, b):
    print('YES')
else:
    print('NO')
