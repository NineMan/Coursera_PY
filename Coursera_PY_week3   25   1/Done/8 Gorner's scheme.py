n = int(input())
x = float(input())

sum = 0
i = n
while i >= 0:
    a = float(input())
    xx = 1
    j = 0
    while j < i:
        xx *= x
        j += 1
    sum += a * xx
    i -= 1
print(sum)
