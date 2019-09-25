import math
p, x, y = int(input()), int(input()), int(input())

sum = x * 100 + y
proc = sum * p // 100
sum_proc = sum + proc
rub = sum_proc // 100
kop = sum_proc % 100

print(rub, kop)
