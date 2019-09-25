def power(a, n):
    exp = 1
    if n == 0:
        return 1
    if n > 0:
        while n > 0:
            exp *= a
            n -= 1
        return exp
    else:
        while n < 0:
            exp *= 1 / a
            n += 1
        return exp


a, n = float(input()),  float(input())
print(power(a, n))
