a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())

if a1 <= b1 <= c1:
    a = a1
    b = b1
    c = c1
elif a1 <= c1 <= b1:
    a = a1
    b = c1
    c = b1
elif b1 <= a1 <= c1:
    a = b1
    b = a1
    c = c1
elif b1 <= c1 <= a1:
    a = b1
    b = c1
    c = a1
elif c1 <= a1 <= b1:
    a = c1
    b = a1
    c = b1
elif c1 <= b1 <= a1:
    a = c1
    b = b1
    c = a1

if a2 <= b2 <= c2:
    x = a2
    y = b2
    z = c2
elif a2 <= c2 <= b2:
    x = a2
    y = c2
    z = b2
elif b2 <= a2 <= c2:
    x = b2
    y = a2
    z = c2
elif b2 <= c2 <= a2:
    x = b2
    y = c2
    z = a2
elif c2 <= a2 <= b2:
    x = c2
    y = a2
    z = b2
elif c2 <= b2 <= a2:
    x = c2
    y = b2
    z = a2

(a1, b1, c1) = (a, b, c)
(a2, b2, c2) = (x, y, z)

if (a1 == a2) and (b1 == b2) and (c1 == c2):
    print('Boxes are equal')
elif (a1 >= a2) and (b1 >= b2) and (c1 >= c2):
    print('The first box is larger than the second one')
elif (a1 <= a2) and (b1 <= b2) and (c1 <= c2):
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')
