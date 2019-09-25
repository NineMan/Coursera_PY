x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
x3, y3 = int(input()), int(input())


def dist4(a, b, c, d):
    x = c - a
    y = d - b
    l = (x ** 2 + y ** 2) ** 0.5
    return l


perimeter = dist4(x1, y1, x2, y2) + dist4(x2, y2, x3, y3) + dist4(x3, y3, x1, y1)
print('{:.6f}'.format(perimeter))