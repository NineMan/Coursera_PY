h = int(input())
a = int(input())
b = int(input())

without_last_day = h - a
in_day = a - b

days = (without_last_day - 1) // in_day + 2

print(days)
