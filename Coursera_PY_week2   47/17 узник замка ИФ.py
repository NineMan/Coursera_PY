a1, b1, c1 = int(input()), int(input()), int(input())
d1, e1 = int(input()), int(input())

if d1 < e1:
    (d, e) = (d1, e1)
else:
    (d, e) = (e1, d1)

if a1 <= b1:
    if b1 <= c1:
        a = a1
        b = b1
        c = c1
    else:
        a = a1
        b = c1
        c = b1
else:
    if a1 <= c1:
        a = a1
        b = b1
        c = c1
    else:
        a = c1
        b = b1
        c = a1

if a < b:
    (a, b) = (a, b)
else:
    (a, b) = (b, a)

if a <= d and b <= e:
    print('YES')
else:
    print('NO')
