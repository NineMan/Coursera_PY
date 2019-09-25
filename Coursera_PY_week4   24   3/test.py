def recurs(n):
    if (n < 10):
        print(n, end=' ')
        return
    else:
        recurs(n // 10)
        print(n % 10, end=' ')
        return


n = int(input())
recurs(n)