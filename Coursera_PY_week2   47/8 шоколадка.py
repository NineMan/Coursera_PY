n = int(input())
m = int(input())
k = int(input())

if (k > (m * n)):
    print('NO')
else:
    if (k % n == 0) or (k % m == 0):
        print('YES')
    else:
        print('NO')
