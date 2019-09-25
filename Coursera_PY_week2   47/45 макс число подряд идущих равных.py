n = int(input())

m = n
number = 0
max_number = 0

while n != 0:
    if m == n:
        number = number + 1
        if max_number < number:
            max_number = number
    else:
        number = 1
    m = n
    n = int(input())
print(max_number)
