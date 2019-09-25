import math

a, b = float(input()), float(input())
c, d = float(input()), float(input())
e, f = float(input()), float(input())

dd = a * d - c * b
dx = d * e - f * b
dy = a * f - c * e

x = dx / dd
y = dy / dd

if (x - int(x) == 0) and (y - int(y) == 0):
    x = int(x)
    y = int(y)
print(x, y)
