def power(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return power(a * a, n // 2)
    return a * power(a, n - 1)


a, n = float(input()), int(input())
print(power(a, n))
