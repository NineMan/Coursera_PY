numberList = list(map(int, input().split()))

i = 0
maxNumber = numberList[0]
maxIndex = 0
minNumber = numberList[0]
minIndex = 0

while i < len(numberList):
    if numberList[i] > maxNumber:
        maxNumber = numberList[i]
        maxIndex = i
    if numberList[i] < minNumber:
        minNumber = numberList[i]
        minIndex = i
    i += 1
numberList[maxIndex] = minNumber
numberList[minIndex] = maxNumber

print(*numberList)
