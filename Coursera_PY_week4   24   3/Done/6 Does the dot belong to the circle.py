x, y = float(input()), float(input())
xc, yc = float(input()), float(input())
rc = float(input())


def IsPointInCircle(a, b, ac, bc, r):
    return (a - ac) ** 2 + (b - bc) ** 2 <= r ** 2


if IsPointInCircle(x, y, xc, yc, rc):
    print('YES')
else:
    print('NO')
