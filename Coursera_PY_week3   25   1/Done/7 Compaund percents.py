p, x, y, k = int(input()), int(input()), int(input()), int(input())

sum = x * 100 + y
i = 0

while i < k:
    sum = sum * (100 + p) // 100
    i += 1

rub = int(sum // 100)
kop = int(sum % 100)

print(rub, kop)
