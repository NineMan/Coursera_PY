numberList = list(map(int, input().split()))

first = False
second = False

for i in numberList:
    if not first:
        first = True
        maxNumber1 = i
    elif not second:
        second = True
        if i >= maxNumber1:
            maxNumber2 = maxNumber1
            maxNumber1 = i
        else:
            maxNumber2 = i
    else:
        if i >= maxNumber1:
            maxNumber2 = maxNumber1
            maxNumber1 = i
        elif i >= maxNumber2:
            maxNumber2 = i

print(maxNumber1, maxNumber2)
