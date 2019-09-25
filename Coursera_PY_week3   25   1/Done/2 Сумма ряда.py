n = int(input())
i = 1
sum = 0
while i <= n:
    sum = sum + 1 / (i ** 2)
    i += 1
if sum - int(sum) == 0:
    print('{:.0f}'.format(sum))
else:
    print(sum)
