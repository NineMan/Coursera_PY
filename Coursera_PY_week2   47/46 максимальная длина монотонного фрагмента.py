now = int(input())

prev = now
prev_prev = now

number = 1
max_number = 0

while now != 0:
    if now == prev:
        number = 1
    elif now > prev:
        if prev >= prev_prev:
            number = number + 1
        else:
            number = 2
    else:
        if prev <= prev_prev:
            number = number + 1
        else:
            number = 2
    if max_number < number:
        max_number = number
#    print(prev_prev, prev, now, number, max_number)
    prev_prev = prev
    prev = now
    now = int(input())

print(max_number)
