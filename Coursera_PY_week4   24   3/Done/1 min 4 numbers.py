a, b, c, d = int(input()), int(input()), int(input()), int(input())


def min4(a, b, c, d):
    n = min(min(min(a, b), c), d)
    return n


print(min4(a, b, c, d))
