#a = int(input())
#b = int(input())
#c = int(input())


def treangle(a, b, c):
    if a <= b:
        if b <= c:
            a1 = a
            b1 = b
            c1 = c
        else:
            a1 = a
            b1 = c
            c1 = b
    else:
        if a <= c:
            a1 = a
            b1 = b
            c1 = c
        else:
            a1 = b
            b1 = c
            c1 = a

    if (a1 == 0) or (b1 == 0) or (c1 == 0):
        print('impossible')
    elif (a1 + b1 <= c1):
        print('impossible')
    elif (a1 * a1 + b1 * b1 == c1 * c1):
        print('rectangular')
    elif (a1 * a1 + b1 * b1 > c1 * c1):
        print('acute')
    elif (a1 * a1 + b1 * b1 < c1 * c1):
        print('obtuse ')
    else:
        print('impossible')

i = 1
j = 1
k = 1
for i in range(3):
    for j in range(3):
        for k in range(3):
            print(i, j, k)
            treangle(i, j, k)



    
