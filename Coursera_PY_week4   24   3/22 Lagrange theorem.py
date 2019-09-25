def lagrange(n, k):
    if k == 0:
        return 1
    if n == 0:
        return 0
    n1 = int(n ** (1 / 2))
    ostat = n - n1 ** 2

    while n1 > 1:
        if lagrange(ostat, k - 1):
            print(n1, end=' ')
        n1 -= 1
#    return 1


n = int(input())
lagrange(n, 4)
