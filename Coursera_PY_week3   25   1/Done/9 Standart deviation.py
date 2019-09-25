x = int(input())

sum = 0
sum_sum = 0
n = 0

while x != 0:
    n += 1
    sum += x
    sum_sum += x * x
    x = int(input())

s = sum_sum - (sum ** 2) / n
s /= n - 1
s = s ** 0.5

print(s)
