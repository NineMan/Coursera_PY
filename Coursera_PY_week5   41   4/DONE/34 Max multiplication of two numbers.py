numberList = list(map(int, input().split()))

minNumber1 = numberList[0]
minNumber2 = numberList[0]
maxNumber1 = numberList[0]
maxNumber2 = numberList[0]

for i in numberList:
    if i > maxNumber1:
        maxNumber2 = maxNumber1
        maxNumber1 = i
    elif i > maxNumber2:
        maxNumber2 = i
    elif i < minNumber1:
        minNumber2 = minNumber1
        minNumber1 = i
    elif i < minNumber2:
        minNumber2 = i
print(maxNumber1, maxNumber2, minNumber2, minNumber1)

if maxNumber1 * maxNumber2 > minNumber1 * minNumber2:
    print(maxNumber2, maxNumber1)
else:
    print(minNumber1, minNumber2)
