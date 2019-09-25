numberList = list(map(int, input().split()))

maxNumber1 = numberList[0]
minNumber1 = numberList[0]
for i in numberList:
    if i > maxNumber1:
        maxNumber1 = i
    elif i < minNumber1:
        minNumber1 = i
min = minNumber1 - 1
max = maxNumber1 + 1

maxNumber1 = min
maxNumber2 = min
maxNumber3 = min
minNumber1 = max
minNumber2 = max
for i in numberList:
    if i > maxNumber1:
        maxNumber3 = maxNumber2
        maxNumber2 = maxNumber1
        maxNumber1 = i
    elif i > maxNumber2:
        maxNumber3 = maxNumber2
        maxNumber2 = i
    elif i > maxNumber3:
        maxNumber3 = i

    if i < minNumber1:
        minNumber2 = minNumber1
        minNumber1 = i
    elif i < minNumber2:
        minNumber2 = i

max1 = maxNumber1 * maxNumber2 * maxNumber3
max2 = maxNumber1 * minNumber1 * minNumber2
# print(maxNumber1, maxNumber2, maxNumber3, minNumber2, minNumber1)
# print(max1, max2)
if max1 > max2:
    print(maxNumber1, maxNumber2, maxNumber3)
else:
    print(maxNumber1, minNumber2, minNumber1)
