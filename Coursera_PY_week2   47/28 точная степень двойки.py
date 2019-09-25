n = int(input())

step = 1
i = 0
while (step < n):
    step = step * 2
    i = i + 1
if step == n:
    print('YES')
else:
    print('NO')
