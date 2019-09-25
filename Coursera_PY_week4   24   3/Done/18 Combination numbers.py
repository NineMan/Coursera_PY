def cnk(n, k):
    if k == n or k == 0:
        return 1
    elif k == 1:
        return n
#    elif n == 0:
#        return 0
    else:
        return cnk(n - 1, k) + cnk(n - 1, k - 1)


n, k = int(input()), int(input())
print(cnk(n, k))
