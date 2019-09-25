l1, w1, h1 = int(input()), int(input()), int(input())
l2, w2, h2 = int(input()), int(input()), int(input())
lc, wc, hc = int(input()), int(input()), int(input())

if (h1 > hc) or (h2 > hc):
    print('NO')
elif h1 + h2 <= hc:
    isBox1InKont = (w1 <= wc and l1 <= lc) or (l1 <= wc and w1 <= lc)
    isBox2InKont = (w2 <= wc and l2 <= lc) or (l2 <= wc and w2 <= lc)
    if isBox1InKont and isBox2InKont:
        print('YES')
    else:
        print('NO')
elif (h1 and h2) <= hc:
    if (l1 + l2 <= lc) and (w1 <= wc) and (w2 <= wc):
        print('YES')
    elif (l1 + w2 <= lc) and (w1 <= wc) and (l2 <= wc):
        print('YES')
    elif (w1 + l2 <= lc) and (l1 <= wc) and (w2 <= wc):
        print('YES')
    elif (w1 + w2 <= lc) and (l1 <= wc) and (l2 <= wc):
        print('YES')

    elif (l1 + l2 <= wc) and (w1 <= lc) and (w2 <= lc):
        print('YES')
    elif (l1 + w2 <= wc) and (w1 <= lc) and (l2 <= lc):
        print('YES')
    elif (w1 + l2 <= wc) and (l1 <= lc) and (w2 <= lc):
        print('YES')
    elif (w1 + w2 <= wc) and (l1 <= lc) and (l2 <= lc):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
