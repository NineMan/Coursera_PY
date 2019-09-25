def rec():
    n = int(input())
    if n != 0:
        if n ** 0.5 == int(n ** 0.5):
            rec()
            print(n, end=' ')
            return 1
        else:
            return rec()
    return


if not rec():
    print(0)
