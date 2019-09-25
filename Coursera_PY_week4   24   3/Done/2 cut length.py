x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())


def distance4(a, b, c, d):
    x = c - a
    y = d - b
    l = (x ** 2 + y ** 2) ** 0.5
    if l == int(l):
        return int(l)
    return l


print(distance4(x1, y1, x2, y2))
