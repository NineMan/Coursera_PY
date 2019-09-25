import math
a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c

if a == 0 and b == 0 and c == 0:
    print(3)
elif a == 0 and b == 0 and c != 0:
    print(0)
elif a == 0:
    x = -c / b
    if (x - int(x) == 0):
        print('1 {:.0f}'.format(x))
    else:
        print('1 {:.6f}'.format(x))

elif d > 0:
    x1 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    if x1 > x2:
        (x1, x2) = (x2, x1)
    if (x1 - int(x1) == 0) and (x2 - int(x2) == 0):
        print('2 {:.0f} {:.0f}'.format(x1, x2))
    else:
        print('2 {:.6f} {:.6f}'.format(x1, x2))

elif d == 0:
    x = - b / (2 * a)
    if x - int(x) == 0:
        print('1 {:.0f}'.format(x))
    else:
        print('1 {:.6f}'.format(x))
else:
    print(0)
