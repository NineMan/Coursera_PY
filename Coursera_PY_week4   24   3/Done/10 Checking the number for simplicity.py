import math
x = int(input())


def MinDivisor(n):
    if n % 2 == 0:
        return 2
    k = 3
    while k <= math.sqrt(n):
        if n % k == 0:
            return k
        k += 2
    return n


def IsPrime(n):
    divisor = MinDivisor(n)
    if divisor == n:
        print('YES')
        return
    print('NO')
    return


IsPrime(x)
