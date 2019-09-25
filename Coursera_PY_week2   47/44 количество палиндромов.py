k = int(input())

number_p = 0
i = 1

while i <= k:
    now_n = i
    old_n = now_n
    new_n = 0
    while (now_n != 0):
        new_n = new_n * 10 + (now_n % 10)
        now_n = now_n // 10
    if (new_n == old_n):
        number_p = number_p + 1
    i = i + 1

print(number_p)
