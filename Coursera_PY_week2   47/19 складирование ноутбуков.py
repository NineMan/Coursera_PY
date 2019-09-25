a, b, c = int(input()), int(input()), int(input())
a1, b1, c1 = int(input()), int(input()), int(input())


max = (a // a1) * (b // b1) * (c // c1)

x = (a // a1) * (b // c1) * (c // b1)
if x > max:
    max = x

x = (a // b1) * (b // a1) * (c // c1)
if x > max:
    max = x

x = (a // b1) * (b // c1) * (c // a1)
if x > max:
    max = x

x = (a // c1) * (b // a1) * (c // b1)
if x > max:
    max = x

x = (a // c1) * (b // b1) * (c // a1)
if x > max:
    max = x

print(max)
