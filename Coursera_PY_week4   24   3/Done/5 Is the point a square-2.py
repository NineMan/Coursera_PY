x, y = float(input()), float(input())


def IsPointInSquare(a, b):
    return (a ** 2) ** 0.5 + (b ** 2) ** 0.5 <= 1


if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
