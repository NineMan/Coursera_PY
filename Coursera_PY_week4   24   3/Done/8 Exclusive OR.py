x, y = int(input()), int(input())


def xor(a, b):
    if (a and not b) or (not a and b):
        return 1
    return 0

print(xor(x, y))
