def phib(a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    return phib(a - 1) + phib(a - 2)


n = int(input())
print(phib(n))
