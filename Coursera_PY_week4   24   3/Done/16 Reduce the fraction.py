def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def ReduceFraction(n, m):
    gcDevision = gcd(n, m)
    n = int(n / gcDevision)
    m = int(m / gcDevision)
    return(n, m)


n, m = int(input()), int(input())
print(*ReduceFraction(n, m))
